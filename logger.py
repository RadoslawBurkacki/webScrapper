#!/bin/env python
import logging
import time
import datetime
import os.path
from os import path

logger = logging.getLogger()
logger.setLevel(logging.INFO)

if not path.exists('logs'):
    os.mkdir('logs')

fh = logging.FileHandler('logs/test.log')
fh.setLevel(logging.INFO) # or any level you want
logger.addHandler(fh)

def log(msg):
    now = datetime.datetime.now()
    date = now.strftime("%d/%m/%Y %H:%M:%S")
    logger.info(date + " " + msg)
    print(date + " " + msg)