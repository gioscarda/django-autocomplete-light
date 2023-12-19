from django.db import models


class Dummy(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    country = models.ForeignKey('cities_light.country', on_delete=models.CASCADE)
    region = models.ForeignKey('cities_light.region', on_delete=models.CASCADE)

    def __unicode__(self):
        return '%s %s' % (self.country, self.region)
