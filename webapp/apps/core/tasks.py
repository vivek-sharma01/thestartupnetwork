from django.conf import settings

import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from celery import shared_task

@shared_task
def send_mail(subject, html_body='', text_body='', sender='contact@thestartupnetwork.in', recipient=''):
    """
    Send Mail Generic Function
    :param subject: subject of mail
    :param html_body: mail body html format
    :param text_body: mail body text format
    :param sender: sender of the mail
    :param recipient: recepient list for mail
    :return:
    """

    smtp_user = settings.EMAIL_HOST_USER
    smtp_password = settings.EMAIL_HOST_PASSWORD
    host = settings.EMAIL_HOST
    port = settings.EMAIL_PORT

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    # part1 = MIMEText(text_body, 'plain')
    part2 = MIMEText(html_body, 'html')
    # msg.attach(part1)
    msg.attach(part2)
    try:
        server = smtplib.SMTP(host, port)
        server.ehlo()
        server.starttls()
        # stmplib docs recommend calling ehlo() before & after starttls()
        server.ehlo()
        server.login(smtp_user, smtp_password)
        server.sendmail(sender, recipient, msg.as_string())
        server.sendmail(sender, sender, msg.as_string())
        server.close()
    except Exception as e:
        print("Error: ", e)
    else:
        print("Email sent!")

