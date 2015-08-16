"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from DiabloDjango.AppCode.DiabloAPI import *


def GetUpdateTime(epochSeconds):
    # Convert SecondsFromEpoch to local datetime
    return datetime.fromtimestamp(epochSeconds)


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
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
    BattleTag = request.GET.get('battletag', '')
    HeroID = request.GET.get('heroid', '')
    Hero = HeroProfile(US_SERVER, BattleTag, HeroID)
    return render(
        request,
        'hero.html',
        context_instance=RequestContext(request,
        {
            'title': 'Diablo 3',
            'year': datetime.now().year,
            #'HeroPortrait': Hero.Portrait,
            'HeroProfile':
                "\nHero Name: " + Hero.Name
                + "\nParagon Level: " + str(Hero.ParagonLevel)
                + "\nClass: " + Hero.Class
                + "\nGender: " + Hero.Gender
                + "\nLast Update: " + str(GetUpdateTime(int(Hero.LastUpdated)))
                + "\n\n\nJSON Dump: \n" + str(Hero),
        })
    )


def career(request):
    """Renders the Career page."""
    assert isinstance(request, HttpRequest)
    BattleTag = request.GET.get('battletagcareer')
    CareerDetails = GetCareer(US_SERVER, BattleTag)
    HeroPortrait = ""
    heroes = CareerDetails.Heroes()
    for hero in heroes:
        HeroPortrait += hero.Portrait
    return render(
        request,
        'career.html',
        context_instance=RequestContext(request,
        {
            'title': 'Diablo 3',
            'year': datetime.now().year,
            'HeroPortrait': HeroPortrait,
            'CareerProfile':
                "\nBattleTag: " + CareerDetails.BattleTag
                + "\nParagon Level: " + str(CareerDetails.ParagonLevel)
                + "\nSeasonal Paragon Level: " + str(CareerDetails.ParagonLevelSeason)
                + "\nElite Kills: " + str(CareerDetails.Kills()['elites'])
                + "\nLast Update: " + str(GetUpdateTime(int(CareerDetails.LastUpdated)))
                + "\n\nHeroes JSON Dump: " + str(CareerDetails.Heroes())
                + "\n\n\nJSON Dump: \n" + str(CareerDetails),
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
