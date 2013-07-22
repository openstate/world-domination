""" Basic models, such as user profile """

from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext as _

from django_countries import CountryField

class Asset(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    continent = models.CharField(max_length=50, choices=(
        ('europe', _('Europe')),
        ('north-america', _('North America')),
        ('south-america', _('South America')),
        ('africa', _('Africa')),
        ('asia', _('Asia')),
        ('australia', _('Australia')),
    ),)
    country = CountryField()
    site = models.ForeignKey(Site)
    
    class Meta:
        ordering = ['continent', 'title']
    
    def __unicode__(self):
        return self.title