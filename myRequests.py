#!/bin/env python
from fake_headers import Headers
import time
import logger
import notify
import requests

header = Headers(
    headers=True  # generate misc headers
)


def makeRequest(URL):
    try:
        page = requests.get(URL, headers=header.generate())
    except requests.exceptions.HTTPError as err:
        print(err)
        logger.log('error when doing request')
        notify.sendEmail("", "Error when doing GET request for scan")
        time.sleep(60)#
    return page
