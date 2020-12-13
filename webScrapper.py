#!/bin/env python
from bs4 import BeautifulSoup
import urllib.request as urllib
import random
import time
import smtplib, ssl
import sys
from email.mime.text import MIMEText
import notify, logger, myRequests
import re

def checkAmazon(product, URL):
    response = myRequests.makeRequest(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    a = soup.find("div", {"id": "availability"})
    soup_string = str(soup)
    b = str(soup)

def checkVery(product, URL):
    found = False
    logger.log("Checking Very for " + product)

    response = myRequests.makeRequest(URL)
    if (type(response) == type(False)):
        logger.log("no response from server")
    else:
        temp = response.text
        print(temp)
        soup = BeautifulSoup(response.content, 'html.parser')
        soup_string = str(soup)
        print(soup_string)

        allProducts = soup.find_all('dd', attrs={'class':'productPrice'})

        for x in allProducts:
            print("looping through listings")
            content = x.text
            content = content.strip()
            content = content.replace('£', '')

            if (float(content) > 400.00): #item over £400 found ps5?
                found = True

        if (found):
            logger.log(product + " is now available")
            notify.sendEmail(product + " is now available on very.com", product + " is now available on very.com")
            notify.playSound()
        else:
            logger.log(product + " not found on very.com")

def checkEbuyer(product, URL):
    found = False
    logger.log("Checking Ebuyer for " + product)

    response = myRequests.makeRequest(URL)
    if (type(response) == type(False)):
        logger.log("no response from server")
    else:
        soup = BeautifulSoup(response.content, 'html.parser')
        soup_string = str(soup)
        allProducts = soup.find_all('p', attrs={'class':'price'})

        for x in allProducts:
            content = x.text
            content = content.strip()
            content = content.replace('£', '')
            content = content.replace(' ', '')
            content = content.replace('\n', '')
            content = content.replace('\xa0inc.vat', '')
            content = content.replace('ex.vat', '')
            if(content != ''):
                if (float(content) > 400.00): #item over £400 found ps5?
                    found = True

        if (found):
            logger.log(product + " is now available")
            notify.sendEmail(product + " is now available on ebuyer.com", product + " is now available on ebuyer.com")
            notify.playSound()
        else:
            logger.log(product + " not found on ebuyer.com")

def checkEbuyerGPUS(product, URL):
    found = False
    logger.log("Checking Ebuyer for " + product)

    response = myRequests.makeRequest(URL)
    if (type(response) == type(False)):
        logger.log("no response from server")
    else:
        soup = BeautifulSoup(response.content, 'html.parser')
        soup_string = str(soup)
        allProducts = soup.find_all('p', attrs={'class':'price'})

        for x in allProducts:
            content = x.text
            content = content.strip()
            content = content.replace('£', '')
            content = content.replace(' ', '')
            content = content.replace('\n', '')
            content = content.replace('\xa0inc.vat', '')
            content = content.replace('ex.vat', '')
            if(content != ''):
                if (float(content) > 650.00): #item over £400 found ps5?
                    found = True

        if (found):
            logger.log(product + " is now available")
            notify.sendEmail(product + " is now available on ebuyer.com", product + " is now available on ebuyer.com")
            notify.playSound()
        else:
            logger.log(product + " not found on ebuyer.com")

def checkcurrys(product, URL):
    found = False
    logger.log("Checking currys for " + product)

    response = myRequests.makeRequest(URL)
    if (type(response) == type(False)):
        logger.log("no response from server")
    else:
        soup = BeautifulSoup(response.content, 'html.parser')
        soup_string = str(soup)
        allProducts = soup.find_all('strong', attrs={'class':'price'})
        soup_string1 = str(allProducts)

        for x in allProducts:
            content = x.text
            content = content.strip()
            content = content.replace('£', '')
            content = content.replace(' ', '')
            content = content.replace('\n', '')
            content = content.replace('\xa0inc.vat', '')
            content = content.replace('ex.vat', '')
            if(content != ''):
                if (float(content) > 400.00): #item over £400 found ps5?
                    found = True

        if (found):
            logger.log(product + " is now available")
            notify.sendEmail(product + " is now available on currys.com", product + " is now available on currys.com")
            notify.playSound()
        else:
            logger.log(product + " not found on currys.com")

while (True):
    checkVery('ps5', "https://www.very.co.uk/e/q/ps5.end?sort=price,0")
    checkEbuyer('ps5', 'https://www.ebuyer.com/1133940-sony-playstation-5-console-cfi-1016a')
    checkEbuyer('5900x', 'https://www.ebuyer.com/1126986-amd-ryzen-9-5900x-am4-processor-100-100000061wof')
    checkEbuyerGPUS('3080', 'https://www.ebuyer.com/store/Components/cat/Graphics-Cards-Nvidia/subcat/GeForce-RTX-3080')
    checkcurrys('ps5', 'https://www.currys.co.uk/gbuk/search-keywords/xx_xx_xx_xx_xx/ps5/1_16/price-desc/xx-criteria.html')


    randomSleepTime = random.randrange(5, 45)
    logger.log("sleep " + str(randomSleepTime))
    time.sleep(randomSleepTime)