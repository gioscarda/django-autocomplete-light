from django.contrib.contenttypes.models import ContentType
from django.db import models
from six import python_2_unicode_compatible

try:
    from django.contrib.contenttypes.fields import GenericForeignKey
except ImportError:
    from django.contrib.contenttypes.generic import GenericForeignKey

try:
    from genericm2m.models import RelatedObjectsDescriptor
except ImportError:
    RelatedObjectsDescriptor = None

try:
    from taggit.managers import TaggableManager
except ImportError:
    TaggableManager = None


@python_2_unicode_compatible
class FkModel(models.Model):
    name = models.CharField(max_length=200)
    relation = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    noise = models.ForeignKey('OtoModel', null=True, blank=True, on_delete=models.CASCADE)

    for_inline = models.ForeignKey('self', null=True, blank=True,
                                   related_name='reverse_for_inline', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


@python_2_unicode_compatible
class OtoModel(models.Model):
    name = models.CharField(max_length=200)
    relation = models.OneToOneField('self', null=True, blank=True, on_delete=models.CASCADE)
    noise = models.ForeignKey('FkModel', null=True, blank=True, on_delete=models.CASCADE)

    for_inline = models.ForeignKey('self', null=True, blank=True,
                                   related_name='inline', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


@python_2_unicode_compatible
class MtmModel(models.Model):
    name = models.CharField(max_length=200)
    relation = models.ManyToManyField('self', blank=True)
    noise = models.ForeignKey('FkModel', null=True, blank=True, on_delete=models.CASCADE)

    for_inline = models.ForeignKey('self', null=True, blank=True,
                                   related_name='inline', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


@python_2_unicode_compatible
class GfkModel(models.Model):
    name = models.CharField(max_length=200)

    content_type = models.ForeignKey(ContentType, null=True, blank=True, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    relation = GenericForeignKey('content_type', 'object_id')

    noise = models.ForeignKey('FkModel', null=True, blank=True, on_delete=models.CASCADE)

    for_inline = models.ForeignKey('self', null=True, blank=True,
                                   related_name='inline', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


if RelatedObjectsDescriptor:
    @python_2_unicode_compatible
    class GmtmModel(models.Model):
        name = models.CharField(max_length=200)
        relation = RelatedObjectsDescriptor()

        noise = models.ForeignKey('FkModel', null=True, blank=True, on_delete=models.CASCADE)
        for_inline = models.ForeignKey('self', null=True, blank=True,
                                       related_name='inline', on_delete=models.CASCADE)

        def __str__(self):
            return self.name


if TaggableManager:
    @python_2_unicode_compatible
    class TaggitModel(models.Model):
        name = models.CharField(max_length=200)
        noise = models.ForeignKey('FkModel', null=True, blank=True, on_delete=models.CASCADE)
        relation = TaggableManager()

        for_inline = models.ForeignKey('self', null=True, blank=True,
                                       related_name='inline', on_delete=models.CASCADE)
        def __str__(self):
            return self.name


@python_2_unicode_compatible
class FullModel(models.Model):
    name = models.CharField(max_length=200)

    oto = models.OneToOneField('self', related_name='reverse_oto', on_delete=models.CASCADE)
    fk = models.ForeignKey('self', related_name='reverse_fk', on_delete=models.CASCADE)
    mtm = models.ManyToManyField('self')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    gfk = GenericForeignKey("content_type", "object_id")

    if RelatedObjectsDescriptor:
        gmtm = RelatedObjectsDescriptor()

    def __str__(self):
        return self.name
