import django
from django.conf import settings

import os
import sys
from os.path import dirname
import datetime
from bs4 import BeautifulSoup
import requests

from slugify import slugify

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
        'slug': slug
    }
    return Location.objects.get_or_create(slug=slug, defaults=data)[0]


def add_membership(price_section):
    """
    Args:
        data:
    Returns:
    """
    from webapp.apps.coworks.models import MembershipBenefits
    from webapp.apps.coworks import constants

    benefit_name = price_section.find('h4').text
    benefit_desc = price_section.find('p').text
    benefit_name = constants.MEMBERSHIPS_DICT[benefit_name]
    benefit_data = {
        'name': benefit_name,
        'description': benefit_desc
    }
    obj, created = MembershipBenefits.objects.get_or_create(name=benefit_name, defaults= benefit_data)
    return obj


def add_amenity(co_amenities_container):
    """"""
    from webapp.apps.coworks.models import Amenity
    amenity_obj_list = []
    for amenity_container in co_amenities_container:
        amenity_name_container = amenity_container.findAll('span')
        for amenity in amenity_name_container:
            amenity_name = amenity.text.strip()
            obj, created = Amenity.objects.get_or_create(name=amenity_name, defaults={'name': amenity_name})
            amenity_obj_list.append(obj)
    return amenity_obj_list


def add_neighbour_amenity(neighbourhood_ameneities_container):
    """"""
    from webapp.apps.coworks.models import NeighbourAmenity
    amenity_obj_list = []
    neighbourhood_amenity = neighbourhood_ameneities_container[0]
    amenities = neighbourhood_amenity.findAll('span')
    descriptions = neighbourhood_amenity.findAll('p')

    for amenity, description in zip(amenities, descriptions):
        data = {
            'name': amenity.text,
            'description': description.text
        }
        obj, created = NeighbourAmenity.objects.get_or_create(name=amenity.text, defaults=data)
        amenity_obj_list.append(obj)
    return amenity_obj_list


def add_contact_person(contact_person_container):
    """"""
    from webapp.apps.coworks.models import ContactPerson
    name = contact_person_container.find('h6').text
    try:
        phone = "".join(contact_person_container.findAll('p')[1].text.split(":")[1].strip().split(" "))[1:][0],
    except:
        phone = "".join(contact_person_container.findAll('p')[1].text.strip().split(" "))[1:]
    print('phone', phone)
    contact_person_data = {
        "description": contact_person_container.findAll('p')[0].text,
        "phone": phone,
        "email": contact_person_container.find('a').text
    }
    contact_person_obj, created = ContactPerson.objects.get_or_create(name=name, defaults=contact_person_data)
    if created:
        return contact_person_obj
    return None


def add_coworks_data():
    """"""

    from webapp.apps.coworks import models

    cities = ['bengaluru', 'chennai', 'mumbai', 'gurgaon']
    for city in cities:
        print('city name:', city)
        location_obj = add_location(city)
        r = requests.get("https://www.cowrks.com/locations/" + city)
        data = r.text
        soup = BeautifulSoup(data, "html.parser")
        data = soup.findAll('div', attrs={'class': 'portfolio-title'})

        for div in data:
            address = div.find('div', attrs={'class': 'co-ban-address'}).text
            link_div = div.find('div', attrs={'class': 'co-new-center-name'})

            link = link_div.find('a')
            cowork_name = link.text.strip()

            r = requests.get(link['href'])
            data = r.text
            soup = BeautifulSoup(data, "html.parser")

            table = soup.findAll('div', attrs={"class": "page-content-change"})
            cowrks_detail = table[0].find('p').text.strip()

            print('cowork_name', cowork_name)

            cowork_data = {
                'address': address,
                'location_id': location_obj.id,
                'name': cowork_name,
                'description': cowrks_detail
            }

            cowork_obj, updated = models.Cowork.objects.update_or_create(name=cowork_name, defaults=cowork_data)

            price_section_divs = soup.findAll('div', attrs={'class': 'co-price-section'})

            for price_section in price_section_divs:
                membership_obj = add_membership(price_section)
                price_div = price_section.find('div', attrs={'class': 'co-price-section-price'})
                try:
                    price = "".join(price_div.find('p').text.strip().split("/")[0].split(","))
                    pricing_obj, created = models.Pricing.objects.get_or_create(cowork_id=cowork_obj.id,
                                                                                membership_id=membership_obj.id,
                                                                                defaults={
                                                                                    'cowork_id': cowork_obj.id,
                                                                                    'membership_id': membership_obj.id,
                                                                                    'price': price
                    })
                except:
                    pass

            co_amenities_container = soup.findAll('div', attrs={"class": "co-amenities-container"})
            amenity_obj_list = add_amenity(co_amenities_container)
            cowork_obj.amenity.add(*amenity_obj_list)
            cowork_obj.save()

            neighbourhood_ameneities_container = soup.findAll('div', attrs={"class": "neighbourhood-ameneities"})
            neighbourhood_ameneities_objs = add_neighbour_amenity(neighbourhood_ameneities_container)
            cowork_obj.neighbour_amenity.add(*neighbourhood_ameneities_objs)
            cowork_obj.save()

            contact_person_container = soup.find('div', attrs={"class": "co-community-info"})
            contact_person_obj = add_contact_person(contact_person_container)
            if contact_person_obj:
                cowork_obj.contact_person_id = contact_person_obj.id
                cowork_obj.save()

            print('cowork object created', )

if __name__ == "__main__":
    SITE_ROOT = os.path.dirname(dirname(os.path.realpath(__file__)))
    sys.path.append(SITE_ROOT)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webapp.settings")
    django.setup()
    add_coworks_data()
