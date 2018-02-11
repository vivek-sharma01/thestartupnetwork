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


def add_location(name, state):
    """
    Args:
        name: name of location
    Returns: location object
    """
    slug = slugify(name)
    from webapp.apps.coworks.models import Location
    data = {
        'name': name.capitalize(),
        'slug': slugify(name),
        'state': state
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

    file_path = os.path.join(BASE_PATH, 'Innov8-Data-new.xlsx')
    data = get_data(file_path)

    # row_list is data of first sheet
    row_list = data['Details _Single Format']
    row_list.pop(0)
    for row in row_list:
        
        cowork_name = row[2]
        address = row[45]
        location_name = 'bengaluru' if row[47].strip() == 'Bangalore' else row[47].strip()
        state = row[48]
        location_obj = add_location(location_name, state)

        cowork_data = {
            'address': address,
            'location_id': location_obj.id,
            'name': cowork_name,
            'website_url': row[5],
            'reasons_to_choose': row[85],
            'locality': row[46],
            'description': row[3]
            # 'price_per_day': row[19],
            # 'price_per_month': row[20],
            # 'no_of_workstattion': row[14]
        }
        cowork_obj, updated = models.Cowork.objects.update_or_create(name=cowork_name, defaults=cowork_data)
        print('cowork name', cowork_obj.name)
        contact_person_data = {
            # "name": row[1],
            "phone": row[6],
            "email": row[4],
            # "alternate_no": row[4   ]
        }

        contact_person_obj, created = models.ContactPerson.objects.get_or_create(email=row[8], defaults=contact_person_data)

        for index in range(53, 59):
            if row[index]:
                benefit_name = constants.MEMBERSHIPS_DICT[row[index]]
                benefit_data = {
                    'name': benefit_name
                    # 'description': benefit_desc
                }
                membership_obj, created = models.MembershipBenefits.objects.get_or_create(name=benefit_name,
                                                                                          defaults=benefit_data)

                if row[index+9]:
                    pricing_data = {
                        'cowork_id': cowork_obj.id,
                        'membership_id': membership_obj.id,
                        'price': row[index+9],

                    }

                    print(pricing_data)
                    pricing_obj, created = models.Pricing.objects.get_or_create(cowork_id=cowork_obj.id,
                                                                                membership_id=membership_obj.id,
                                                                                defaults= pricing_data)

        amenity_obj_list = []
        for index in range(8, 42):
            if row[index]:
                amenity_name = row[index].strip()
                obj, created = models.Amenity.objects.get_or_create(name=amenity_name, defaults={'name': amenity_name})
                amenity_obj_list.append(obj)

        cowork_obj.amenity.add(*amenity_obj_list)
        cowork_obj.save()


if __name__ == "__main__":
    SITE_ROOT = os.path.dirname(dirname(os.path.realpath(__file__)))
    sys.path.append(SITE_ROOT)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webapp.settings")
    django.setup()
    add_data()
