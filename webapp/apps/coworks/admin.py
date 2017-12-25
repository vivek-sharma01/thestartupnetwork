from django.contrib import admin

from . import models

admin.site.register(models.Cowork)
admin.site.register(models.MembershipBenefits)
admin.site.register(models.Pricing)
admin.site.register(models.ContactPerson)
admin.site.register(models.Amenity)
admin.site.register(models.NeighbourAmenity)
admin.site.register(models.Location)