"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
#from django.template import RequestContext
from datetime import datetime
from DiabloDjango.AppCode import DiabloAPI
from DiabloDjango.AppCode.DiabloObjects import DiabloAPIConfig
from DiabloDjango.AppCode.DiabloObjects import Career
from DiabloDjango.AppCode.DiabloObjects import Hero

import traceback
import sys

def GetUpdateTime(epochSeconds):
    # Convert SecondsFromEpoch to local datetime
    return datetime.fromtimestamp(epochSeconds)


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    context = {
            'title': 'Diablo 3',
            'year': datetime.now().year,
        }
    return render(
        request,
        'index.html',
        context
    )


def career(request):
    """Renders the Career page."""
    assert isinstance(request, HttpRequest)
    BattleTag = request.GET.get('battletagcareer')
    if not BattleTag:
        CareerDetails = Career.Career(request.session['CareerProfile'])
    else:
        CareerDetails = DiabloAPI.GetCareer(DiabloAPIConfig.US_SERVER, BattleTag)
        request.session['CareerProfile'] = CareerDetails
    HeroPortrait = ""
    heroes = CareerDetails.Heroes()
    for hero in heroes:
        HeroPortrait += hero.Portrait
    context_instance = {
        'Title': 'Diablo 3',
        'Year': datetime.now().year,
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
    }
    return render(
        request,
        'career.html',
        context_instance
    )

def handler400(request):
    response = render_to_response('error.html', {}, context_instance=RequestContext(request))
    response.status_code = 400
    return response

def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response

def handler500(request):
    #response = render_to_response('500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    context_instance = {
        "error": "Test Return"
    }
    return render(
        request,
        '500.html',
        context_instance
    )


def hero(request):
    """Renders the hero page."""
    assert isinstance(request, HttpRequest)
    HeroID = request.GET.get('heroid', '')
    CareerProfile = Career.Career(request.session['CareerProfile'])
    Heroes = CareerProfile.Heroes()
    CurrentHero = list()
    # If HeroID not passed in use current hero or last played hero
    if not HeroID:
        CurrentHero = Hero.Hero(request.session['CurrentHero'])
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

    context_instance = {
        'Title': 'Diablo 3',
        'Year': datetime.now().year,
        'UserName': CareerProfile.BattleTagDisplay,
        'Damage': "{:,}".format(CurrentHero.Damage),
        'HeroName': CurrentHero.Name,
        'CharacterMenu': HeroPortrait,
        'HeroVitru': CurrentHero.BackImage,
        'HandsIcon': CurrentHero.Hands.IconURL,
        'HandsToolTip': CurrentHero.Hands.ToolTipURL,
        'ChestIcon': CurrentHero.Chest.IconURL,
        'ChestToolTip': CurrentHero.Chest.ToolTipURL,
        'LegsIcon': CurrentHero.Legs.IconURL,
        'LegsToolTip': CurrentHero.Legs.ToolTipURL,

        'AttackStats': '<div><span>Damage</span><span>' + "{:,}".format(CurrentHero.Damage) + '</span></div>'
            + '<div><span>Critical Hit Chance</span><span>' + str(CurrentHero.CriticalChance) + "%" + '</span></div>'
            + '<div><span>Critical Hit Damage</span><span>' + str(CurrentHero.CriticalDamage) + "%" + '</span></div>'
            + '<div><span>Attack Speed</span><span>' + str(CurrentHero.AttackSpeed) + '</span></div>',

        'LifeStats': '<div><span>Life</span><span>' + "{:,}".format(CurrentHero.Life) + '</span></div>'
            + '<div><span>Life On Hit</span><span>' + "{:,}".format(CurrentHero.LifeOnHit) + '</span></div>'
            + '<div><span>Toughness</span><span>' + "{:,}".format(CurrentHero.Toughness) + '</span></div>'
            + '<div><span>Healing</span><span>' + "{:,}".format(CurrentHero.Healing) + '</span></div>'
            + '<div><span>Armor</span><span>' + "{:,}".format(CurrentHero.Armor) + '</span></div>',

        'ResistanceStats': '<div><span>Cold</span><span>' + "{:,}".format(CurrentHero.ColdResist) + '</span></div>'
            + '<div><span>Fire</span><span>' + "{:,}".format(CurrentHero.FireResist) + '</span></div>'
            + '<div><span>Physical</span><span>' + "{:,}".format(CurrentHero.PhysicalResist) + '</span></div>'
            + '<div><span>Arcane</span><span>' + "{:,}".format(CurrentHero.ArcaneResist) + '</span></div>',

        'BuffStats': '<div><span>Magic Find Percent</span><span>' + "{:,}".format(CurrentHero.MagicFind) + '%</span></div>'
            + '<div><span>Gold Find Percent</span><span>' + "{:,}".format(CurrentHero.GoldFind) + '%</span></div>'
            + '<div><span>Life Steal</span><span>' + "{:,}".format(CurrentHero.LifeSteal) + '</span></div>'
            + '<div><span>Damage Increase</span><span>' + "{:,}".format(CurrentHero.DamageIncrease) + '</span></div>'
            + '<div><span>Damage Reduction</span><span>' + "{:,}".format(CurrentHero.DamageReduction) + '</span></div>',

        'StatList': CurrentHero.statList,

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
    }

    return render(
        request,
        'hero.html',
        context_instance
    )


def toolbox(request):
    """Renders the Toolbox page."""
    assert isinstance(request, HttpRequest)
    BattleTag = request.GET.get('battletagcareer')
    if not BattleTag:
        CareerDetails = Career.Career(request.session['CareerProfile'])
    else:
        CareerDetails = DiabloAPI.GetCareer(DiabloAPIConfig.US_SERVER, BattleTag)
        request.session['CareerProfile'] = CareerDetails
    HeroPortrait = ""
    heroes = CareerDetails.Heroes()
    for hero in heroes:
        HeroPortrait += hero.Portrait
    context_instance = {
        'Title': 'Diablo 3',
        'Year': datetime.now().year,
        'UserName': CareerDetails.BattleTagDisplay,
        'CharacterMenu': HeroPortrait,
    }
    return render(
        request,
        'toolbox.html',
        context_instance
    )


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    context_instance = {
        'title': 'Contact',
        'message': 'Your contact page.',
        'year': datetime.now().year,
    }
    return render(
        request,
        'contact.html',
        context_instance
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    context_instance = {
        'title': 'About',
        'message': 'Your application description page.',
        'year': datetime.now().year,
    }
    return render(
        request,
        'about.html',
        context_instance
    )
