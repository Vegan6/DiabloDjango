from django.shortcuts import render
from django.http import HttpRequest
#from django.template import RequestContext
from datetime import datetime
from DiabloDjango.AppCode import DiabloAPI
from DiabloDjango.AppCode.DiabloObjects import DiabloAPIConfig
from DiabloDjango.AppCode.DiabloObjects import Career
from DiabloDjango.AppCode.helper import *
from DiabloDjango.AppData import models


def GetCareer(userid, seasonid, localeid):
    User = models.DimensionUser.objects.get(userid=userid, localeid=locale)
    if not models.FactCareer.objects.filter(serID=user, SeasonID=seasonid).exists():
        #Call API and update
        Locale = models.DimensionLocale.objects.get(localeid=localeid)
        CareerDetails = DiabloAPI.GetCareer(Locale.LocaleNameAPI, User.BattleTag)
        CurrentCareer = UpdateCareer(userid, CareerDetails)
        return CurrentCareer
    else:
        CurrentCareer = models.FactCareer.objects.get(userid=user, SeasonID=seasonid)
        return CurrentCareer


def UpdateCareer(userid, careerdetails):
    User = models.DimensionUser.objects.get(userid=userid)
    if not models.FactCareer.objects.filter(userid=User, seasonid=seasonid).exists():
        CareerDetails = DiabloAPI.GetCareer(DiabloAPIConfig.US_SERVER, BattleTag)
        CheckCareer = models.FactCareer(
            UserID=User, SeasonID=seasonid, ParagonLevel=CareerDetails.ParagonLevel

            )
        CheckCareer.save()
    else:
        CheckCareer = models.FactCareer.objects.get(UserID=User, SeasonID=seasonid)
        return


def UpdateUser(battletag, locale):
    DisplayTag = battletag.replace('-', '#')
    #User = models.DimensionUser.objects.get(battletag=battletag)
    if not models.DimensionUser.objects.filter(battletag=battletag, localeid=locale).exists():
        User = models.DimensionUser(battletag=battletag, battletagdisplay=DisplayTag, lastupdated=datetime.now(), localeid=locale)
        User.save()
    else:
        User = models.DimensionUser.objects.get(battletag=battletag, localeid=locale)
        User.lastupdated = datetime.now()
        User.save(update_fields=['lastupdated'])
    return User


def GetActProgHTML(actProg):
    if actProg:
        return '<span class="actprogcomplete">Completed</span>'
    else:
        return '<span class="actprogincomplete">Incomplet</span>'


def career(request):
    """Renders the Career page."""
    assert isinstance(request, HttpRequest)
    #Locale = models.DimensionLocale.objects.get(localenameapi='en_US')
    BattleTag = request.GET.get('battletagcareer')
    #UserID = UpdateUser(BattleTag, Locale)
    if not BattleTag:
        CareerDetails = Career.Career(request.session['CareerProfile'])
    else:
        #CareerDetails = GetCareer(UserID, -1, 1)
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
        'Act1Completed': GetActProgHTML(CareerDetails.Act1Completed),
        'Act2Completed': GetActProgHTML(CareerDetails.Act2Completed),
        'Act3Completed': GetActProgHTML(CareerDetails.Act3Completed),
        'Act4Completed': GetActProgHTML(CareerDetails.Act4Completed),
        'Act5Completed': GetActProgHTML(CareerDetails.Act5Completed),
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