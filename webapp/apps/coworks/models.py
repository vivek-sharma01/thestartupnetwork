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
    amenity = models.ManyToManyField('coworks.amenity', related_name='cowork_amenities', blank=True, null=True)
    neighbour_amenity = models.ManyToManyField('coworks.neighbouramenity', related_name='cowork_neighbouramenities',
                                               blank=True, null=True)
    contact_person = models.ManyToManyField('coworks.contactperson', related_name='cowork_contactperson',
                                            blank=True, null=True)
    location = models.ForeignKey('coworks.location', related_name='location_coworks', null=True, blank=True)
    website_url = models.CharField(max_length=500, null=True, blank=True)
    price_per_day = models.CharField(max_length=50, null=True, blank=True)
    price_per_month = models.CharField(max_length=50, null=True, blank=True)
    no_of_workstattion = models.CharField(max_length=50, null=True, blank=True)
    banner_image = models.ImageField(upload_to='banner_image/', null=True, blank=True)
    parent_cowork = models.CharField(max_length=300, null=True, blank=True)
    locality = models.CharField(max_length=300, null=True, blank=True)
    objects = managers.CoworkManager()

    def __str__(self):
        return self.name or ''

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Cowork, self).save(*args, **kwargs)

    def get_pricing(self):
        """get pricing related to membership"""
        memberships = Pricing.objects.filter(cowork_id=self.id).values('membership__name', 'membership__description',
                                                                       'price', 'membership__suitable_for', 'suitable_for')
        response = []
        class_list = [
            {'business-card': 'business-card-body'},
            {'meeting-card': 'meeting-card-body'},
            {'virtual-office-card': 'virtual-office-card-body'},
            {'business-card': 'business-card-body'},
            {'meeting-card': 'meeting-card-body'},
            {'virtual-office-card': 'virtual-office-card-body'},
            {'business-card': 'business-card-body'},
            {'meeting-card': 'meeting-card-body'},
            {'virtual-office-card': 'virtual-office-card-body'}
        ]

        for index, membership in enumerate(memberships):
            for heading_class, suitable_class in class_list[index].items():
                obj = {
                    'name': constants.MEMBERSHIPS_REVERSE_DICT[membership['membership__name']],
                    'description': membership['membership__description'],
                    'price': membership['price'],
                    'heading_class': suitable_class,
                    'suitable_class': heading_class,
                    'suitable_for': membership['suitable_for']
                }
                response.append(obj)
        return response

    def get_minimum_price(self):
        """minimum price for a cowork"""
        return self.price_per_month
        # memberships = Pricing.objects.filter(cowork_id=self.id).values_list('price', flat=True)
        # return min(memberships) if memberships else None

    def get_location_name(self):
        return self.location.name

    def get_url(self):
        """"""
        return "/coworks/india/{}/{}/".format(self.location.slug, self.slug)


class MembershipBenefits(models.Model):
    """Membership benefits for cowork"""
    name = models.CharField(max_length=300, choices=constants.MEMBERSHIPS, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    suitable_for = ArrayField(models.CharField(max_length=200), blank=True, null=True)

    def __str__(self):
        return self.name or ''

    def get_name(self):
        """name of benefit"""
        return constants.MEMBERSHIPS_REVERSE_DICT[self.name]


class Pricing(models.Model):
    """pricing for cowork based on membership"""
    cowork = models.ForeignKey(Cowork, related_name="cowork_price", null=True, blank=True)
    membership = models.ForeignKey(MembershipBenefits, related_name="membership_price", null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    time_unit = models.CharField(max_length=30, null=True, blank=True)
    time_value = models.CharField(max_length=30, null=True, blank=True)
    seats = models.PositiveIntegerField(null=True, blank=True)
    suitable_for = ArrayField(models.CharField(max_length=200), blank=True, null=True)

    def __str__(self):
        return self.cowork.name + ": " + self.membership.name + ": " + str(self.price) or ''


class Amenity(models.Model):
    """Amenities for cowork"""
    name = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name or ''


class NeighbourAmenity(models.Model):
    """Amenities for cowork"""
    name = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name or ''


class ContactPerson(models.Model):
    """Contact Person for cowork"""
    name = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    email = models.CharField(max_length=254, null=True, blank=True)
    alternate_no = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name or ''


class Location(models.Model):
    """Location Model"""
    name = models.CharField(max_length=300, null=True, blank=True)
    slug = models.SlugField(max_length=300, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name or ''

    def get_url(self):
        """"""
        return '/coworks/{}'.format(self.slug)

    def name_capitalize(self):
        """"""
        return " ".join(list(map(lambda x: x.capitalize(), self.name.split())))