# -*- coding: utf-8 -*-
from __future__ import print_function
import smtplib

def check_email(username,password,smtp_host='smtp.gmail.com',smtp_port=587):
    if type(username) != str or type(password) != str :
        raise Exception("Username / Password must be of type String")
    server = smtplib.SMTP()
    server.connect(smtp_host,smtp_port)
    server.ehlo()
    server.starttls()
    try:
        server.login(username,password)
        print("Two step Verification not detected")
    except smtplib.SMTPAuthenticationError, msg:
        if "Application-specific password required" in msg[1]:
            print("Two Step Verification Detected ")
        elif "Username and Password not accepted" in msg[1]:
            print("Incorrect Username or Password , Please provide correct username and password to test the account. ")
        else:
            print("some unknown error.."+msg[1]) 
            