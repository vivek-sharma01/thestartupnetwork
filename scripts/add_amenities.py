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



# @transaction.atomic
def add_data():
    """
    this fn save 91 springboard data in db
    """

    from pyexcel_xls import get_data

    BASE_PATH = os.path.dirname(os.path.realpath(__file__))
    from webapp.apps.coworks import models, constants

    file_path = os.path.join(BASE_PATH, 'Filters_25 Jan_v1.1.xlsx')
    data = get_data(file_path)

    # row_list is data of first sheet
    row_list = data['Amenities Filters']
    row_list.pop(0)

    for row in row_list:
        for index, col in enumerate(row[1:]):
            
            amenity_filter = constants.AMENITIES_FILTER_INDEX[index+1]
            name = col
            amenity_data = {
                'name': name,
                'filter': amenity_filter
            }
            amenity, updated = models.Amenity.objects.update_or_create(name=name, defaults=amenity_data)
            if updated:
                print('amenity updated with filter {}'.format(amenity.filter))
            else:
                print('amenity created with filter {}'.format(amenity.filter))

if __name__ == "__main__":
    SITE_ROOT = os.path.dirname(dirname(os.path.realpath(__file__)))
    sys.path.append(SITE_ROOT)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webapp.settings")
    django.setup()
    add_data()
