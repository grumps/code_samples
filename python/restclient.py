""""
This class interacts with an api, the data returned from the api
is passed into a serializer framework that created application "objects"
that and handled in a celery task queue.

This class is executed in a task queue as well, not all functions/methods are 
here, names might be funky to protect the identity.
"""

# tasks.py

@task
def run_pipeline(pipeline_id, start_time, end_time):
    """
    Runs an import process for a single pipeline
    :param pipeline_id int: id of the pipeline
    :param start_time datetime.datetime: start time
    :param end_time datetime.datetime: end time
    """
    pipeline = PosPipeline.objects.get(id=pipeline_id)
    for data in pipeline.get_data_imports(start_time, end_time):
        data_class = apps.get_model('transactions', 'TransactionImport')
        actual_start_time = data.pop("start_time")
        actual_end_time = data.pop("end_time")
        data["pipeline_id"] = pipeline.id
        created_data = data_class.objects.create(**data)
        status = JobStatus.objects.get(machine_name="ip")
        job = DataPipeLineJob(pipeline=pipeline,
                              job_status=status,
                              start_time=actual_start_time,
                              end_time=actual_end_time)
        # create a group of tasks, then update the job status.
        result = chord((create_transaction_subitems.si(i["serializer"],
                                                       i["field_mapping"],
                                                       created_data.id)
                        for i in pipeline.subitems()),
                       update_pipeline_job(job.id))

# models.py


class SomeSystem(SomeOtherClass):
    """
    This class represents a connection to the REST Api. It doesn"t specifically store
    any information about the connection parameters, it expects them to be provided. The
    configuration should come in the way of a the :class:`Config`. The configuration
    should contain *at least* two properties. So to setup a connection, one should call:
    py:method:`setup` first, then utilize methods within this class to extra data from
    the API.
    A :class:`Config.auth_config` should contain the following parameters:
    :param api_token str: the token for a specific merchant
    :param some_id str: the some_id for the conneciton.
    """
    SOME_CONFIG = ("api_token", "some_id",)
    SOME_API_HEADERS = {"Authorization": "api_token"}
    BASE = "https://some.thing.on.the.wing"
    SOME_VERSION = "v3"
    BASE_SLUG = "eee"
    URL_CONF = (BASE, SOME_VERSION, SOME_SLUG)
    FilterParam = namedtuple("FilterParam", ["field", "equality", "value"])
    Expand = namedtuple("Expand", ["value", ])
    Limit = namedtuple("Limit", ["offset", "limit"])

    def get_url(self, slug):
        """
        Builds URL for making a request based on the slug.
        Utilizes contstances that are set within the class.
        e.g. HOST_NAME etc
        :param slug str: the slug to hit e.g. "orders"
        :return url: URL for the request
        :rtype str:
        """
        merch_id_slug = (self.connection_config[self.SOME_CONFIG[1]], slug)
        return "/".join((self.URL_CONF + merch_id_slug))

    @classmethod
    def dt_to_unixstamp(cls, dt):
        if isinstance(dt, datetime.datetime):
            epoch = datetime.datetime.utcfromtimestamp(0)
            return int((dt - epoch).total_seconds() * 1000.0)

    def setup(self, config, start_time, end_time):
        """
        Sets up headers and connection parameters. Limits api response to the timedelta
        provided.
        :param config :class:`posdata.RestConfig`: configuration for this connection
        :param start_date :class:`datetime.datetime`: start time for this connection
        :param end_date :class:`datetime.datetime`: end time for this connection
        """
        if hasattr(config, "auth_config"):
            self.connection_config = config.auth_config
            self.set_headers()
            self.start_time = self.dt_to_unixstamp(start_time)
            self.end_time = self.dt_to_unixstamp(end_time)

    def set_headers(self):
        """set the headers on the request object"""
        headers = {}
        try:
            for key, token in self.SOME_API_HEADERS.iteritems():
                value = self.connection_config[token]
                # Not great here... adding the `Bearer` perm
                # not sure why it would need to change tho
                headers.update({key: "Bearer %s" % value})
        except AttributeError:
            raise AttributeError(
                "setup_connection must be called before any requests are made")
        self.headers = headers

    def _build_params(self, params):
        """
        Takes a list of parameters defined using :class:`.CloverSystem.FilterParam`
        or :class:`.CloverSystem.Expand`, makes a completed flattened string.
        This isn't the greatest! It's far more complex that I'd like it to be.
        :param params list: list of :class:`.CloverSystem.FilterParam` or :class:`.CloverSystem.Expand`
        :returns: flattened params
        :rtype: str
        """

        assert isinstance(
            params, list), "Params should be list of NamedTuple Values"
        filter_strings = []
        expand_strings = []
        # there should only be one.
        limits_string = ""
        for param in params:
            if isinstance(param, self.FilterParam):
                filter_strings.append("{}{}{}".format(param.field,
                                                      param.equality,
                                                      param.value))
            elif isinstance(param, self.Expand):
                expand_strings.append["{}".format(f.value)]
            elif isinstance(param, self.Limit):
                # there should be only one limit and offeset param.
                limits_string = "limit={}&offset={}".format(
                    param.limit,
                    param.offset)
            else:
                raise TypeError("Unsupported Param Type")
        # I know not every pythonic style, so shoot me mmk?
        # basically we're trying to avoid extra "&" and params into the url
        filter_string = "filter=" + \
            "&".join(filter_strings) if filter_strings else None
        expand_string = "expand=" + \
            "&".join(expand_strings) if expand_strings else None
        limit_string = limits_string if limits_string != "" else None
        final_strings = [x for x in [filter_string,
                                     expand_string, limit_string] if x is not None]
        return "&".join(final_strings)

    def request(self, slug, **kwargs):
        """
        A shortcut to py:module:`requests.request` that takes nearly
        the same signature as the request function with one change.
        Method can be taking as a kwarg, but defaults to "GET"
        Limit params, should be directly added, as a kwargs, if added
        as param, you'll likely get unexpected results, because this is a
        recurisive function.
        :param slug str: the slug of the url, the base hosts and slugs are combined.
        :returns data: all data for the required time period
        :rtype dict:
        """
        method = kwargs.get("method", "GET")
        kwargs.update({"headers": self.headers})
        url = self.get_url(slug)
        supplied_params = kwargs.get("params", [])
        # avoid mutability issues during recursion
        params = list(supplied_params)
        params.append(self.FilterParam("createdTime", ">=", self.start_time))
        params.append(self.FilterParam("createdTime", "<=", self.end_time))
        # remove limit from kwargs, because we don't want to pass that down
        # to the requests package
        try:
            limit = kwargs.pop("limit")
        except KeyError:
            limit = self.Limit(offset=0, limit=500)
        params.append(limit)
        # This is not so hot but the way this api wants some,
        # params doesn't play so well with requests package
        built_params = self._build_params(params)
        built_kwargs = dict(kwargs)
        built_kwargs["params"] = built_params
        response = requests.request(method, url, **built_kwargs).json()
        elements = response.get("elements")
        # base case
        if len(response.get("elements")) == 0:
            try:
                return self._response_data
            except AttributeError:
                # This is if we end on the first iteration
                return response
        else:
            try:
                self._response_data["elements"].extend(elements)
            except AttributeError:
                self._response_data = response
            new_offest = limit.offset + limit.limit
            new_limit = self.Limit(offset=new_offest, limit=limit.limit)
            # always provide the orginal params.
            return self.request(slug, limit=new_limit,
                                params=supplied_params)

    def _get_max_min_date_range(self):
        """
        Get the oldest and newest date for the instance"s `self.initial_data`
        :returns min_date, max_date
        :rtype tuple:
        """
        timestamp_key = "createdTime"
        max_date = max(self.initial_data, key=itemgetter(timestamp_key))
        min_date = min(self.initial_data, key=itemgetter(timestamp_key))
        return (min_date["createdTime"], max_date["createdTime"])
