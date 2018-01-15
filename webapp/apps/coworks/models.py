from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

from . import managers, constants
from webapp.apps import gen_hash, expires


class ModelBase(models.Model):
    """
        This is a abstract model class to add is_deleted, created_at and modified at fields in any model
    """
    id = models.CharField(primary_key=True, max_length=30)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def soft_delete(self, *args, **kwargs):
        """ Soft delete """
        self.is_deleted = True
        self.save()

    def hard_delete(self, *args, **kwargs):
        """Hard delete"""
        self.delete()

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = gen_hash(expires())
        super(ModelBase, self).save(*args, **kwargs)


class Cowork(ModelBase):
    """Cowork detail model"""
    name = models.CharField(max_length=300, null=True, blank=True)
    slug = models.SlugField(max_length=300, unique=True)
    description = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    landmark = models.TextField(null=True, blank=True)
    amenity = models.ManyToManyField('coworks.amenity', related_name='cowork_amenities', blank=True)
    neighbour_amenity = models.ManyToManyField('coworks.neighbouramenity', related_name='cowork_neighbouramenities',
                                               blank=True)
    contact_person = models.ManyToManyField('coworks.contactperson', related_name='cowork_contactperson', blank=True)
    location = models.ForeignKey('coworks.location', related_name='location_coworks', null=True, blank=True)
    website_url = models.CharField(max_length=500, null=True, blank=True)
    price_per_day = models.CharField(max_length=50, null=True, blank=True)
    price_per_month = models.CharField(max_length=50, null=True, blank=True)
    no_of_workstattion = models.CharField(max_length=50, null=True, blank=True)

    objects = managers.CoworkManager()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Cowork, self).save(*args, **kwargs)

    def get_pricing(self):
        """get pricing related to membership"""
        memberships = Pricing.objects.filter(cowork_id=self.id).values('membership__name', 'membership__description',
                                                                       'price')
        response = []
        for membership in memberships:
            obj = {
                'name': membership['membership__name'],
                'description': membership['membership__description'],
                'price': membership['price']

            }
            response.append(obj)
        return response

    def get_minimum_price(self):
        """minimum price for a cowork"""
        memberships = Pricing.objects.filter(cowork_id=self.id).values_list('price', flat=True)
        return min(memberships) if memberships else None


class MembershipBenefits(models.Model):
    """Membership benefits for cowork"""
    name = models.CharField(max_length=300, choices=constants.MEMBERSHIPS, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    suitable_for = ArrayField(models.CharField(max_length=200), blank=True, null=True)

    def __str__(self):
        return self.name

    def get_name(self):
        """name of benefit"""
        return constants.MEMBERSHIPS_REVERSE_DICT[self.name]


class Pricing(models.Model):
    """pricing for cowork based on membership"""
    cowork = models.ForeignKey(Cowork, related_name="cowork_price", null=True)
    membership = models.ForeignKey(MembershipBenefits, related_name="membership_price", null=True)
    price = models.FloatField(null=True, blank=True)
    time_unit = models.CharField(max_length=30, null=True, blank=True)
    time_value = models.CharField(max_length=30, null=True, blank=True)
    seats = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.cowork.name + ": " + self.membership.name + ": " + str(self.price)


class Amenity(models.Model):
    """Amenities for cowork"""
    name = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class NeighbourAmenity(models.Model):
    """Amenities for cowork"""
    name = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class ContactPerson(models.Model):
    """Contact Person for cowork"""
    name = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=254, null=True, blank=True)
    alternate_no = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    """Location Model"""
    name = models.CharField(max_length=300, null=True, blank=True)
    slug = models.SlugField(max_length=300, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_url(self):
        """"""
        return '/coworks/{}'.format(self.slug)

    def name_capitalize(self):
        """"""
        return " ".join(list(map(lambda x: x.capitalize(), self.name.split())))