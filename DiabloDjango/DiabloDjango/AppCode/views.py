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
    CareerProfile = Career(request.session['CareerProfile'])
    Heroes = CareerProfile.Heroes()
    CurrentHero = list()
    # If HeroID not passed in use current hero or last played hero
    if not HeroID:
        CurrentHero = Hero(request.session['CurrentHero'])
        if not CurrentHero:
            HeroID = int(CareerProfile.LastHeroPlayed)
            for hero in Heroes:
                if hero.HeroId == HeroID:
                    CurrentHero = hero
    else:
        HeroID = int(HeroID)
        for hero in Heroes:
            if hero.HeroId == HeroID:
                CurrentHero = hero
    # Grab Details for the Hero portraits
    HeroPortrait = ""
    heroes = CareerProfile.Heroes()
    for hero in heroes:
        HeroPortrait += hero.Portrait

    request.session['CurrentHero'] = CurrentHero
    return render(
        request,
        'hero.html',
        context_instance=RequestContext(request,
        {
            'Title': 'Diablo 3',
            'Year': datetime.now().year,
            'UserName': CareerProfile.BattleTagDisplay,
            'HeroPortrait': HeroPortrait,
            'Damage': "{:,}".format(CurrentHero.Damage),
            'HeroName': CurrentHero.Name,
            'Portrait': CurrentHero.Portrait,
            'CharacterMenu': HeroPortrait,
            'HeroProfile':
                "\nHero Name: " + CurrentHero.Name
                + "\nParagon Level: " + str(CurrentHero.ParagonLevel)
                + "\nClass: " + CurrentHero.Class
                + "\nGender: " + CurrentHero.Gender
                + "\nCritical Hit Chance: " + str(CurrentHero.CriticalChance) + "%"
                + "\nCritical Hit Damage: " + str(CurrentHero.CriticalDamage) + "%"
                + "\nLast Update: " + str(GetUpdateTime(int(CurrentHero.LastUpdated)))
                + "\nDamage: " + str(CurrentHero.Damage)
                + "\n\n\nJSON Dump: \n" + str(CurrentHero),
        })
    )


def career(request):
    """Renders the Career page."""
    assert isinstance(request, HttpRequest)
    BattleTag = request.GET.get('battletagcareer')
    if not BattleTag:
        CareerDetails = Career(request.session['CareerProfile'])
    else:
        CareerDetails = GetCareer(US_SERVER, BattleTag)
        request.session['CareerProfile'] = CareerDetails
    HeroPortrait = ""
    heroes = CareerDetails.Heroes()
    for hero in heroes:
        HeroPortrait += hero.Portrait
    return render(
        request,
        'career.html',
        context_instance=RequestContext(request,
        {
            'Title': 'Diablo 3',
            'Year': datetime.now().year,
            'HeroPortrait': HeroPortrait,
            'UserName': CareerDetails.BattleTagDisplay,
            'CharacterMenu': HeroPortrait,
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
