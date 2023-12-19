from django.db import models


class Address(models.Model):
    city = models.ForeignKey('cities_light.city', related_name='address_inline_set', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
