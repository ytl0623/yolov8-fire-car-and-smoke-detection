import requests
import json
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
import getpass
from bs4 import BeautifulSoup


def send_email():
    your_email = "david89062388@gmail.com"
    your_password =
    send_email_to = "bitcointest0206@gmail.com"

    # create message object instance
    msg = MIMEMultipart()

    # the parameters of the message
    password = your_password
    msg['From'] = your_email
    msg['To'] = send_email_to
    msg['Subject'] = "ASAP! Detected burning car incident"

    text = MIMEText('<img src="cid:image1">', 'html')
    msg.attach(text)

    image = MIMEImage(open('runs/detect/test1.jpg', 'rb').read())

    # Define the image's ID as referenced in the HTML body above
    image.add_header('Content-ID', '<image1>')
    msg.attach(image)

    # create the gmail server
    server = smtplib.SMTP("smtp.gmail.com: 587")

    server.starttls()

    # Login Creds for sending the email
    server.login(msg['From'], password)

    # sends the message
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    print("\nSend Email!!!\n")
    server.quit()
