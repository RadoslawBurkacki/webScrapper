#!/bin/env python
import smtplib, ssl
import sys
from email.mime.text import MIMEText
import notify
from playsound import playsound
from email.mime.text import MIMEText
import logger

def playSound():
    playsound('test.mp3')

def sendEmail(subject, msg):
    port = 465  # For SSL
    password = "1sobeliny2"

    # Create a secure SSL context
    context = ssl.create_default_context()

    fromx = 'radek111a@gmail.com'
    to  = 'radekb333@gmail.com'
    msg = MIMEText(msg)
    msg['Subject'] = subject
    msg['From'] = fromx
    msg['To'] = to

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("radek111a@gmail.com", password)
        # TODO: Send email here
        server.sendmail("radek111a@gmail.com", "radekb333@gmail.com", msg.as_string())
    logger.log("email send, exit program")
