""" Views for the base application """
from pprint import pprint

from django.shortcuts import render
from django.contrib.sites.models import get_current_site

from .models import Asset

def home(request):
    """ Default view for the root """
    
    site = get_current_site(request)
    assets = Asset.objects.filter(site=site).all()
    #pprint(assets)

    ordered_assets = {}
    for asset in assets:
        existing = ordered_assets.get(asset.continent, [])
        existing.append(asset)
        ordered_assets[asset.continent] = existing

    pprint(ordered_assets)

    return render(request, 'base/home.html', {
        'site': site,
        'assets': ordered_assets
    })
