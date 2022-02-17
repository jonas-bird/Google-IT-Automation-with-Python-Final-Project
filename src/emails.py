#!/usr/bin/env python3
"""
Script to handle sending email reports for Final Project Google IT Automation
With Python 
Jonas Bird
2021-12-28 
"""
import smtplib
from email.message import EmailMessage
import mimetypes
import os.path


def generate_error_report(sender, reciever, subject, body):
    return generate_report(sender, reciever, subject, body, attachment=None)


def generate_report(sender, reciever, subject, body, attachment):
    message = EmailMessage()
    message['From'] = sender
    message['To'] = reciever
    message['Subject'] = subject
    message.set_content(body)
    if attachment is not None:
        attachment_path = attachment
        attachment_filename = os.path.basename(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split('/', 1)
        with open(attachment_path, 'rb') as ap:
            message.add_attachment(ap.read(),
                                   maintype=mime_type,
                                   subtype=mime_subtype,
                                   filename=attachment_filename)
    return message


def send_email(message):
    # TODO switch mailtrap testing code for prod code
    # with smtplib.SMTP('localhost') as server:
    #     mail_server.send_message( message)
    print(message)
    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        server.login("971e262f4551f0", "a325b73c808dd1")
        server.send_message(message)
