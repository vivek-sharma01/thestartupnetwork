from django.template.loader import render_to_string

from . import models, serializers, constants
from webapp.apps.core import tasks

from dateutil.parser import parse


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
        pass

    reason = constants.ENQUIRY_REASON[data.get('reason')].format(request_date)
    mail_text = constants.MEMBERSHIP_ENQUIRY_MAIL_TEXT.format(cowork.name, reason, data['name'],
                                                              data['phone'], data['email'])

    mail_subject = constants.MEMBERSHIP_ENQUIRY_MAIL_SUBJECT.format(reason)

    tasks.send_mail(subject=mail_subject, html_body=mail_text, recipient='ashutosh9sharma@gmail.com')


def send_mail_to_customer(data, cowork):
    """send mails to cowork"""
    request_date = None
    try:
        request_date = parse(data['request_date']).date()
    except:
        pass

    reason = constants.ENQUIRY_REASON[data.get('reason')].format(request_date)
    # mail_text = constants.MEMBERSHIP_ENQUIRY_MAIL_TEXT.format(cowork.name, reason, data['name'],
    #                                                           data['phone'], data['email'])

    mail_subject = constants.MEMBERSHIP_ENQUIRY_MAIL_SUBJECT.format(reason)
    # import ipdb;ipdb.set_trace()
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
    tasks.send_mail(subject=mail_subject, html_body=html_content, recipient='ashutosh9sharma@gmail.com')
