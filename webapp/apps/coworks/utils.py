from django.template.loader import render_to_string

from . import models, serializers, constants
from webapp.apps.core import tasks

from dateutil.parser import parse
import datetime


def get_locations():
    """"""
    cowork_location = models.Location.objects.all()
    location_serializer = serializers.LocationSerializer(cowork_location, many=True)
    return location_serializer.data


def extract_membership_name(membership):
    return constants.MEMBERSHIPS_ORDERING[constants.MEMBERSHIPS_DICT[membership.get('name')]]


def send_mail_to_cowork(data, cowork):
    """send mails to cowork"""
    request_date = None
    try:
        request_date = parse(data['request_date']).date()
    except:
        request_date = datetime.datetime.today()
        pass

    reason = constants.ENQUIRY_REASON[data.get('reason')].format(request_date)
    mail_text = constants.CONTACT_US_MAIL_TEXT.format(cowork.name, reason, data['name'],
                                                              data['phone'], data['email'])

    mail_subject = constants.MEMBERSHIP_ENQUIRY_MAIL_SUBJECT.format(reason)

    try:
        contact_person_email = cowork.contact_person.all()[0].email
        tasks.send_mail.delay(subject=mail_subject, html_body=mail_text, recipient=contact_person_email)

    except:
        pass


def send_membership_mail_to_cowork(data, cowork):
    """"""
    request_date = None
    try:
        request_date = parse(data['request_date']).date()
    except:
        pass

    reason = constants.ENQUIRY_REASON[data.get('reason')].format(request_date)
    membership_type = constants.MEMBERSHIPS_REVERSE_DICT[data['metadata']['membership_type']]
    mail_text = constants.MEMBERSHIP_ENQUIRY_MAIL_TEXT.format(cowork.name, reason, data['name'],
                                                              data['phone'], data['email'],
                                                              membership_type,
                                                              data['metadata']['no_of_person'])

    mail_subject = constants.MEMBERSHIP_ENQUIRY_MAIL_SUBJECT.format(reason)
    try:
        contact_person_email = cowork.contact_person.all()[0].email
        tasks.send_mail(subject=mail_subject, html_body=mail_text, recipient=contact_person_email).delay()
    except:
        pass


def send_mail_to_customer(data, cowork):
    """send mails to cowork"""
    request_date = None
    try:
        request_date = parse(data['request_date']).date()
    except:
        pass
    reason = constants.ENQUIRY_REASON[data.get('reason')].format(request_date)
    mail_subject = constants.MEMBERSHIP_ENQUIRY_MAIL_SUBJECT.format(reason)
    contact_obj = cowork.contact_person.all()
    mail_data = {
        'cowork_name': cowork.name,
        'cowork_address': cowork.address,
        'data': data,
        'request_date': request_date
    }
    if contact_obj:
        obj = {
            'email': contact_obj.email,
            'name': contact_obj.name
        }
        mail_data.update(obj)

    html_content = render_to_string('membership-customer-email.html', mail_data)
    email = data['email']
    tasks.send_mail(subject=mail_subject, html_body=html_content, recipient=email).delay()
