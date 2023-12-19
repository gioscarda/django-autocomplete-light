from django.db import models
from six import python_2_unicode_compatible


@python_2_unicode_compatible
class OnTheFly(models.Model):
    name = models.CharField(max_length=100)
    other_fly = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
