import json
import logging
from json import JSONDecodeError

import requests
from allure import step, attach
from allure_commons.types import AttachmentType
from curlify import to_curl


def attach_request_log(response):
    with step("Attaching body, status code and curl to allure"):
        try:
            json_dump = json.dumps(response.json(), indent=3)
            attach(body=json_dump, name='json', attachment_type=AttachmentType.JSON, extension='.json')
        except JSONDecodeError:
            text = response.text
            attach(body=text, name='text', attachment_type=AttachmentType.TEXT, extension='.txt')
        curl = to_curl(response.request)
        status_code = f"Status code: {response.status_code}"
        attach(body=status_code, name='status_code', attachment_type=AttachmentType.TEXT, extension='.txt')
        attach(body=curl, name='curl', attachment_type=AttachmentType.TEXT, extension='.txt')
    with step("Logging status code and curl into console"):
        logging.info(f"Status code: {status_code}")
        logging.info(f"cURL: {curl}")


def post_demowebshop(url, **kwargs):
    with step(f"POST {url}"):
        response = requests.post(url=url, **kwargs)
        attach_request_log(response)
        return response
