import requests
import json
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import getpass
from bs4 import BeautifulSoup

def send_email( i ):
    your_email = "david89062388@gmail.com"
    your_password = "tehxfalyzkkdplcn"
    send_email_to = "bitcointest0206@gmail.com"
                   
    # create message object instance
    msg = MIMEMultipart()

    # the parameters of the message
    password = your_password
    msg['From'] = your_email
    msg['To'] = send_email_to
    msg['Subject'] = "Warning"

    # your message
    if ( i == 0 ):
        message = "Warning Smoke!!!"
    elif ( i == 1 ):
        message = "Warning Fire!!!"

    # adds in the message from the above variable
    msg.attach(MIMEText( message, "plain" ) )

    # create the gmail server
    server = smtplib.SMTP( "smtp.gmail.com: 587" )

    server.starttls()

    # Login Creds for sending the email
    server.login( msg['From'], password )

    # sends the message
    server.sendmail( msg['From'], msg['To'], msg.as_string() )
    
    print("\nSend Email!!!\n")
    server.quit()


