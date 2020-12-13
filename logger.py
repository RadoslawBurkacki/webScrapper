#!/bin/env python
import logging
import time
import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)
fh = logging.FileHandler('logs/test.log')
fh.setLevel(logging.INFO) # or any level you want
logger.addHandler(fh)


def log(msg):
    now = datetime.datetime.now()
    date = now.strftime("%d/%m/%Y %H:%M:%S")
    logger.info(date + " " + msg)
    print(date + " " + msg)