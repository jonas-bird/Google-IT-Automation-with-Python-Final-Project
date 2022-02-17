#!/usr/bin/env python3
"""
This script performs background monitoring for some system statistics
Part of The final project for Google's IT Automation with Python, using
material
Jonas Bird
2021-12-28
"""

import shutil
import psutil
import socket
from emails import generate_error_report, send_email

sender = 'automation@example.com'
reciever = 'jBird@importantcompany.com'  # change to reflect proper userID
email_body='Please check your system and resolve the issue as soon as possible'
subjects = {
    'disk_full': "Available disk space is lower than 20%",
    'CPU_high': "CPU usage us over 80%",
    'low_memory': "Available memory is less than 500MB",
    'hostname': "localhost cannot be resolved to 127.0.0.1"
}


def check_cpu(percent):
    """
    Return True if CPU utilization is over the provided percent for more
    than 0.5 seconds
    """
    # return True
    percent_cpu = psutil.cpu_percent(interval=1.0)
    if percent_cpu > percent:
        return True
    return False


def check_disk_full(disk, min_percent):
    """Return True if there isn't enough disk space, false otherwise"""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    if percent_free < min_percent:
        return True
    return False


def check_memory(memory_threshold):
    """
    Return True if there is less available memory than the provided amount
    in the parameters
    """
    free_memory = psutil.virtual_memory().total
    if free_memory / 1024 / 1024 < memory_threshold:
        return True
    return False


def check_localhost():
    """"
    Return True if there is a problem with the loopback
    """
    if socket.gethostbyname('localhost') == '127.0.0.1':
        return False
    return True


def main():
    """
    Code to run if the script is run
    """
    cpu_percent = 80
    storage_percent = 20
    free_mem_amount = 500
    if check_disk_full(disk="/", min_percent=storage_percent):
        subject = subjects['disk_full']
    elif check_memory(free_mem_amount):
        subject = subjects['low_memory']
    elif check_cpu(cpu_percent):
        subject = subjects['CPU_high']
    elif check_localhost():
        subject = subjects['hostname']
    else:
        return 0

    email_data = generate_error_report(sender, reciever,
                                       subject, email_body)
    send_email(email_data)
    return 0


if __name__ == "__main__":
    main()
