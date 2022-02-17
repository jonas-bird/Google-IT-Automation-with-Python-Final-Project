#!/usr/bin/env python3

import os
import datetime
from reports import generate_pdf
from emails import generate_report, send_email

path_to_pdf  = '/tmp/processed.pdf'
# path_to_pdf = '/home/jonas/Projects/W4/processed.pdf'
path_to_descriptions = "supplier-data/descriptions/"
date_generated = datetime.datetime.now().strftime('%Y-%m-%d')


def create_body(path_to_descriptions):
    files = os.listdir(path_to_descriptions)
    descriptions = ""
    for file in files:
        if file.endswith('.txt'):
            with open(path_to_descriptions + file, 'r') as f:
                lines = f.readlines()
                title = lines[0].rstrip()
                amount = lines[1].rstrip()
                descriptions += "name: " + title + "<br/>" + "weight: " + amount + "<br/><br/>"
    return descriptions


def main():
    # create attachment
    body = create_body(path_to_descriptions)
    title = "Processed Updated on " + date_generated
    generate_pdf(body, title, path_to_pdf)

    # generate email
    # TODO swap test email for productiion ones
    sender = 'automation@example.com'
    reciever = 'jBird@importantcompany.com'
    #   reciever = insert student id@example.com
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    email_to_send = generate_report(sender, reciever, subject, body, path_to_pdf)
    # send the email on out
    send_email(email_to_send)

    return 0


if __name__ == "__main__":
    main()
