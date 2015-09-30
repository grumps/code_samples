import cStringIO
import hashlib

from flask import request, jsonify
import requests as rq

from skullduggery import app
from skullduggery.util import InvalidAPIUsage
from skullduggery.process import process
import settings


@app.route('/')
@app.route('/index')
def index():
    raise InvalidAPIUsage('Not Authorized.', status_code=403)


@app.route('/skullduggery', methods=['POST'])
def skullduggery():
    if request.method == 'POST':
        form_clean, form_cleaned = clean(request.form)
        try:
            if form_clean:
                image = get_image(form_cleaned['url'])
                image_url = create_url(process(image), form_cleaned['url'], form_cleaned['user_name'])
                return jsonify(json_response(image_url, form_cleaned['user_name']))
        except KeyError:
            raise InvalidAPIUsage('Data Missing', status_code=404)


@app.errorhandler(InvalidAPIUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


def clean(form):
    """
    DOESN'T REALLY CLEAN
    :param form:
    :return form_cleaned:
    """
    form_cleaned = {}
    try:
        if form['token'] == str(settings.slack_token):
            try:
                form_temp = {}
                for key in form.keys():
                    for value in form.getlist(key):
                        form_temp[key] = str(value)
                form_clean = True
                lindex = form_temp['text'].index('<') + 1
                rindex = form_temp['text'].index('>')
                url = form_temp['text'][lindex:rindex]
                form_temp['url'] = url
                form_temp.__delitem__('text')
                form_cleaned = form_temp
            except ValueError:
                raise InvalidAPIUsage('Image URL Not Found', status_code=404)
            except KeyError:
                raise InvalidAPIUsage('Inavlide data found', status_code=401)
            finally:
                return form_clean, form_cleaned
        else:
            raise InvalidAPIUsage('Token Incorrect', status_code=403)
    except KeyError:
        raise InvalidAPIUsage('Token Missing', status_code=401)



def get_image(someurl):
    """
    :param someurl:
    :settings.satic:
    :return PIL imageobj:
    """
    content_types = ('image/png', 'image/jpeg', 'image/jpg')
    response = rq.get(someurl)
    if response.headers['content-type'] in content_types:
        return cStringIO.StringIO(response.content)
    else:
        raise InvalidAPIUsage('Image not found or Content Type' + response.headers['content-type'], status_code=401)

def create_url(image, url, requestor):
    """
    :param image:
    :param url:
    :return full image url:
    """
    uid = hashlib.md5(url).hexdigest()
    slug = settings.static_url + "skullduggery_for_" + requestor + "_" + uid + ".jpg"
    image.save(slug, "JPEG")
    return request.url_root + slug


def json_response(url, user):
    response = {
    "text": "skullduggeryme: for " + user + " " + url,
    "username": "Skulldeggerybot",
    "icon_emoji": ":skullz:"
    }
    return response