import os
import time
import datetime
import smtplib                             # optional (advanced)
from email.mime.multipart         import * # optional (& advanced)
from email.mime.text              import * # optional (& advanced)
from email.message                import * # optional
from colorama                     import *
from art                          import *

# initializing colorama
init()

#email function  (optional & advanced)
# def gmail_send(subject, message, from, to, pass):
#     global link
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login(from, pass)
#     msg            = EmailMessage()
#     message        = f'{message}'
#     msg.set_content(message)
#     msg['Subject'] = subject
#     msg['From']    = from
#     msg['To']      = to
#     server.send_message(msg)

new_entry = input("ENTER DIARY ENTRY HERE >>>")

with open("copy.txt", "a") as file:
    file.write(new_entry)
