"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime, timedelta
from DiabloDjango.AppCode.DiabloAPI import *

# Convert SecondsFromEpoch to local datetime


def GetUpdateTime(epochSeconds):
    return datetime.fromtimestamp(epochSeconds)


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    #query = request.GET.get('hello', '')
    return render(
        request,
        'index.html',
        context_instance=RequestContext(request,
        {
            'title': 'Diablo 3',
            'year': datetime.now().year,
        })
    )


def hero(request):
    """Renders the hero page."""
    assert isinstance(request, HttpRequest)
    if (request.GET.get('GetHero')):
        BattleTag = request.GET.get('battletag')
        HeroID = int(request.GET.get('heroid'))
        Hero = HeroProfile(US_SERVER, BattleTag, HeroID)
    else:
        Hero = ''
    return render(
        request,
        'hero.html',
        context_instance=RequestContext(request,
        {
            'title': 'Diablo 3',
            'year': datetime.now().year,
            'HeroProfile':
                "\nHero Name: " + Hero['name']
                + "\nParagon Level: " + str(Hero['paragonLevel'])
                + "\nClass: " + Hero.Class()
                + "\nGender: " + Hero.Gender()
                + "\nLast Update: " + str(GetUpdateTime(int(Hero['last-updated']))),
        })
    )


def career(request):
    """Renders the Career page."""
    assert isinstance(request, HttpRequest)
    if (request.GET.get('GetCareer')):
        BattleTag = request.GET.get('battletagcareer')
        CareerDetails = GetCareer(US_SERVER, BattleTag)
        CareerKills = CareerDetails.Kills()
    else:
        CareerInfo = ''
    return render(
        request,
        'hero.html',
        context_instance=RequestContext(request,
        {
            'title': 'Diablo 3',
            'year': datetime.now().year,
            'HeroProfile':
                "\nBattleTag: " + CareerDetails['battleTag']
                + "\nParagon Level: " + str(CareerDetails['paragonLevel'])
                + "\nSeasonal Paragon Level: " + str(CareerDetails['paragonLevelSeason'])
                + "\nElite Kills: " + str(CareerKills['elites'])
                + "\nHeroes: " + str(CareerDetails.Heroes())
                + "\nLast Update: " + str(GetUpdateTime(int(CareerDetails['lastUpdated']))),
        })
    )


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'Pages/contact.html',
        context_instance=RequestContext(request,
        {
            'title': 'Contact',
            'message': 'Your contact page.',
            'year': datetime.now().year,
        })
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'Pages/about.html',
        context_instance=RequestContext(request,
        {
            'title': 'About',
            'message': 'Your application description page.',
            'year': datetime.now().year,
        })
    )
