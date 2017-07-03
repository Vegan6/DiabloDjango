from django.shortcuts import render
from django.http import HttpRequest
#from django.template import RequestContext
from datetime import datetime
from DiabloDjango.AppCode import DiabloAPI
from DiabloDjango.AppCode.DiabloObjects import DiabloAPIConfig
from DiabloDjango.AppCode.DiabloObjects import Career
from DiabloDjango.AppCode.helper import *


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
    CareerTable = ""
    heroes = CareerDetails.Heroes()
    for hero in heroes:
        HeroPortrait += hero.Portrait
        CareerTable += hero.CareerTableRow
    context_instance = {
        'Title': 'Diablo 3',
        'Year': datetime.now().year,
        'UserName': CareerDetails.BattleTagDisplay,
        'CharacterMenu': HeroPortrait,
        'BattleTag': CareerDetails.UserName,
        'GuildName': CareerDetails.GuildName,
        'CareerTable': CareerTable,
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