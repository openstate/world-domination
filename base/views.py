""" Views for the base application """

from django.shortcuts import render
from django.contrib.sites.models import get_current_site

def home(request):
    """ Default view for the root """
    
    site = get_current_site(request)
    return render(request, 'base/home.html', {
        'site': site
    })
