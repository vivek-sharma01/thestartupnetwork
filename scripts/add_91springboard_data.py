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


def add_location(name):
    """
    Args:
        name: name of location
    Returns: location object
    """
    slug = slugify(name)
    from webapp.apps.coworks.models import Location
    data = {
        'name': name.capitalize(),
        'slug': slugify(name)
    }
    return Location.objects.get_or_create(slug=slug, defaults=data)[0]

# @transaction.atomic
def add_data():
    """
    this fn save 91 springboard data in db
    """

    from pyexcel_xls import get_data

    BASE_PATH = os.path.dirname(os.path.realpath(__file__))
    from webapp.apps.coworks import models, constants

    file_path = os.path.join(BASE_PATH, '91springboardhublistings.xlsx')
    data = get_data(file_path)

    # row_list is data of first sheet
    row_list = data['Sheet1']
    row_list.pop(0)

    new_row_list = []
    for index in range(1,19):
        temp_list = []

        for i, row in enumerate(row_list):
            print(row[0])
            try:
                temp_list.append(row[index])
            except:
                pass
        new_row_list.append(temp_list)

    for index, row in enumerate(new_row_list):
        name = row[0].split(",")
        cowork_name = ",".join(name[:2])
        print(cowork_name)
        address = row[5]

        location_name = 'bengaluru' if row[32].strip() == 'Bangalore' else row[32]
        location_obj = add_location(location_name)
        cowork_data = {
                'address': address,
                'location_id': location_obj.id,
                'name': cowork_name,
                'website_url': row[30],
                'price_per_day': row[19],
                'price_per_month': row[20],
                'no_of_workstattion': row[14]
            }

        cowork_obj, updated = models.Cowork.objects.update_or_create(name=cowork_name, defaults=cowork_data)

        contact_person_data = {
            "name": row[1],
            "phone": row[2].strip(),
            "email": row[3],
            "alternate_no": row[4].strip()
        }
        try:
            contact_person_obj, created = models.ContactPerson.objects.get_or_create(name=name, defaults=contact_person_data)
        except:
            contact_person_data = {
                # "name": row[1],
                "phone": row[1].strip(),
                "email": row[2],
                "alternate_no": row[3].strip()
            }
            contact_person_obj, created = models.ContactPerson.objects.get_or_create(name=name,
                                                                                     defaults=contact_person_data)

        for index in [9, 10, 11, 12, 13]:
            if row[index] == 'Yes':
                benefit_name = constants.MEMBERSHIPS_DICT[constants.MEMBERSHIPS_91SPRINGBOARD_MAPPING[index]]
                benefit_data = {
                    'name': benefit_name
                    # 'description': benefit_desc
                }
                membership_obj, created = models.MembershipBenefits.objects.get_or_create(name=benefit_name,
                                                                                          defaults=benefit_data)

                if benefit_name == 'ES':
                    pricing_data = {
                        'cowork_id': cowork_obj.id,
                        'membership_id': membership_obj.id,
                        'price': row[26],
                        'time_unit': 'hours',
                        'time_value': '4'
                    }
                    pricing_obj, created = models.Pricing.objects.get_or_create(cowork_id=cowork_obj.id,
                                                                                membership_id=membership_obj.id,
                                                                                defaults= pricing_data)

                    pricing_data = {
                        'cowork_id': cowork_obj.id,
                        'membership_id': membership_obj.id,
                        'price': row[27],
                        'time_unit': 'hours',
                        'time_value': '8'
                    }
                    pricing_obj, created = models.Pricing.objects.get_or_create(cowork_id=cowork_obj.id,
                                                                                membership_id=membership_obj.id,
                                                                                defaults=pricing_data)



if __name__ == "__main__":
    SITE_ROOT = os.path.dirname(dirname(os.path.realpath(__file__)))
    sys.path.append(SITE_ROOT)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webapp.settings")
    django.setup()
    add_data()
