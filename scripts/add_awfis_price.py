import os
import sys
from os.path import dirname
import datetime

import django
from django.db import transaction


from slugify import slugify

# To run the script run python webapp/apps/cms/scripts/fund_manager_data.py from
# your virtual env. Make sure you have mf_product_data.xlsx in your webapp/apps/cms/scripts/
# make sure you run pip install -r requirements.txt and check pyexcel-io==0.2.1
# pyexcel-xls==0.2.1 and xlrd==1.0.0 is installed in your virtual env


def add_pricing(cowork, membership, pricing_data):
    """"""
    from webapp.apps.coworks import models, constants
    if pricing_data['price'] != 'N.A.' and pricing_data['price'] != 'N.A':
        obj = models.Pricing.objects.create(**pricing_data)
        print('pricing object created for cowork {} membership {} pricing data {}'.format(cowork, membership,
                                                                                              pricing_data))


# @transaction.atomic
def add_data():
    """
    this fn save 91 springboard data in db
    """

    from pyexcel_xls import get_data

    BASE_PATH = os.path.dirname(os.path.realpath(__file__))
    from webapp.apps.coworks import models, constants

    file_path = os.path.join(BASE_PATH, 'Awfis Details.xlsx')
    data = get_data(file_path)

    # row_list is data of first sheet
    row_list = data['Price']
    row_list.pop(0)

    new_row_list = []

    for row in row_list:
        cowork = models.Cowork.objects.get(name=row[0])

        membership = models.MembershipBenefits.objects.get(name='PS')
        pricing_data = {
            'cowork_id': cowork.id,
            'membership_id': membership.id,
            'price': row[1],
            'time_unit': 'month',
            'time_value': '1',
            'seats': 1
        }
        add_pricing(cowork, membership, pricing_data)

        membership = models.MembershipBenefits.objects.get(name='DD')
        pricing_data = {
            'cowork_id': cowork.id,
            'membership_id': membership.id,
            'price': row[2],
            'time_unit': 'day',
            'time_value': '1',
            'seats': 1
        }
        add_pricing(cowork, membership, pricing_data)

        pricing_data = {
            'cowork_id': cowork.id,
            'membership_id': membership.id,
            'price': row[3],
            'time_unit': 'week',
            'time_value': '1',
            'seats': 1
        }
        add_pricing(cowork, membership, pricing_data)

        pricing_data = {
            'cowork_id': cowork.id,
            'membership_id': membership.id,
            'price': row[4],
            'time_unit': 'month',
            'time_value': '1',
            'seats': 1
        }
        add_pricing(cowork, membership, pricing_data)

        membership = models.MembershipBenefits.objects.get(name='FD')
        pricing_data = {
            'cowork_id': cowork.id,
            'membership_id': membership.id,
            'price': row[5],
            'time_unit': 'day',
            'time_value': '1',
            'seats': 1
        }
        add_pricing(cowork, membership, pricing_data)

        pricing_data = {
            'cowork_id': cowork.id,
            'membership_id': membership.id,
            'price': row[6],
            'time_unit': 'week',
            'time_value': '1',
            'seats': 1
        }
        add_pricing(cowork, membership, pricing_data)

        pricing_data = {
            'cowork_id': cowork.id,
            'membership_id': membership.id,
            'price': row[7],
            'time_unit': 'month',
            'time_value': '1',
            'seats': 1
        }
        add_pricing(cowork, membership, pricing_data)

        membership = models.MembershipBenefits.objects.get(name='CR')
        pricing_data = {
            'cowork_id': cowork.id,
            'membership_id': membership.id,
            'price': row[8],
            'time_unit': 'hour',
            'time_value': '1',
            'seats': 4
        }
        add_pricing(cowork, membership, pricing_data)

        pricing_data = {
            'cowork_id': cowork.id,
            'membership_id': membership.id,
            'price': row[9],
            'time_unit': 'day',
            'time_value': '1',
            'seats': 4
        }
        add_pricing(cowork, membership, pricing_data)

        pricing_data = {
            'cowork_id': cowork.id,
            'membership_id': membership.id,
            'price': row[10],
            'time_unit': 'hour',
            'time_value': '1',
            'seats': 6
        }
        add_pricing(cowork, membership, pricing_data)

        pricing_data = {
            'cowork_id': cowork.id,
            'membership_id': membership.id,
            'price': row[11],
            'time_unit': 'day',
            'time_value': '1',
            'seats': 6
        }
        add_pricing(cowork, membership, pricing_data)

        pricing_data = {
            'cowork_id': cowork.id,
            'membership_id': membership.id,
            'price': row[12],
            'time_unit': 'hour',
            'time_value': '1',
            'seats': 8
        }
        add_pricing(cowork, membership, pricing_data)

        pricing_data = {
            'cowork_id': cowork.id,
            'membership_id': membership.id,
            'price': row[8],
            'time_unit': 'day',
            'time_value': '1',
            'seats': 8
        }
        add_pricing(cowork, membership, pricing_data)

if __name__ == "__main__":
    SITE_ROOT = os.path.dirname(dirname(os.path.realpath(__file__)))
    sys.path.append(SITE_ROOT)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webapp.settings")
    django.setup()
    add_data()
    # add_amenities()