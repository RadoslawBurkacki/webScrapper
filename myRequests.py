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
        s=time.time()
        print("doing request for " + URL)
        page = requests.get(URL, headers=header.generate(), timeout=10)
    except requests.exceptions.Timeout as err:
        print(err)
        logger.log('error when doing request')
        time.sleep(1)#
        return False
    return page
