from locust import Locust, TaskSet, task
import URLManager


class ProgramFinder(TaskSet):

    """
    Class TaskSet for for the Program Finder and Program Details.
    """
    sort_param = ['redacted']
    program_details = ['redacted']

    def on_start(self):
        response = self.client.get('/explore-our-programs')
        print response.status_code

    @task(5)
    def sort(self):
        num_of_param = len(self.sort_param)
        winning_param = URLManager.getRandom(num_of_param) - 1
        response = self.client.get(self.sort_param[winning_param])
        print response.status_code

    @task(10)
    def detail(self):
        num_of_details = len(self.program_details)
        winning_detail = URLManager.getRandom(num_of_details) - 1
        response = self.client.get(self.program_details[winning_detail])
        print response.status_code

    @task(1)
    def end_program(self):
        self.interrupt()


class SimpleTest(TaskSet):

    """
    Class handles a simple baseline test of Homepage and Standard Content Page.
    """

    standard_content_pages = ['/for-parents/invest-in-your-childs-future', '/for-parents/safety-and-supervision',
                              '/for-parents/preparing-for-the-program']

    @task
    def standardpage(self):
        num_of_urls = len(self.standard_content_pages)
        winning_url = URLManager.getRandom(num_of_urls) - 1
        self.client.get(self.standard_content_pages[winning_url])
        print "standard content type"


class LoadTest(TaskSet):

    def on_start(self):
        response = self.client.get('/')
        print response.status_code

    tasks = {ProgramFinder: 5, SimpleTest: 1}


class MyLocust(Locust):
    task_set = LoadTest
    min_wait = 5000
    max_wait = 15000
