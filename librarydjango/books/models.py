""" Books Models """

# Django
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save

# Utilities
import uuid

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    image = models.CharField(max_length=516, null=True, blank=True)
    slug = models.SlugField(null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

def set_slug(sender, instance, *args, **kwargs):
    """ Set automatic slug to new books """
    if instance.title and not instance.slug:
        slug = slugify(instance.title)

        while Book.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.title, str(uuid.uuid4())[:8])
            )
        instance.slug = slug

pre_save.connect(set_slug, sender=Book)


