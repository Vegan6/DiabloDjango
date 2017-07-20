from django.shortcuts import render
from django.http import HttpRequest
#from django.template import RequestContext
from datetime import datetime
from DiabloDjango.AppCode import DiabloAPI
#from DiabloDjango.AppCode.DiabloObjects import DiabloAPIConfig
from DiabloDjango.AppCode.DiabloObjects import Career
from DiabloDjango.AppCode import helper
from DiabloDjango.AppData import models
from django.core import serializers
import re


# Step 1 Insert career if not there, pull if it is
# Step 2 Insert career if not there, update & pull if it is (async?)
#On Update Career - Need to Insert/Update Hereoes listed (fallen and alive)
def GetCareer(userid, locale):
    User = models.DimensionUser.objects.get(userid=userid, localeid=locale.localeid)
    #Locale = models.DimensionLocale.objects.get(localeid=localeid)
    CareerDetails = DiabloAPI.GetCareer(locale.serverurl, User.battletag)
    CurrentCareer = UpdateCareer(userid, CareerDetails)
    return CurrentCareer


def UpdateCareer(userid, careerdetails):
    User = models.DimensionUser.objects.get(userid=userid)
    seasonid = -1
    if not models.FactCareer.objects.filter(userid=User, seasonid=seasonid).exists():
        #Still need artisan levels
        CheckCareer = models.FactCareer(
            userid=User, seasonid=seasonid, paragonlevel=careerdetails.ParagonLevel,
            paragonlevelhardcore=careerdetails.ParagonLevelHardcore, paragonlevelseason=careerdetails.ParagonLevelSeason,
            paragonlevelseasonhardcore=careerdetails.ParagonLevelSeasonHardcore, guildname=careerdetails.GuildName,
            lastheroplayed=careerdetails.LastHeroPlayed, lastupdateddatetime=helper.GetUpdateTime(careerdetails.LastUpdated),
            monsterkills=careerdetails.MonsterKills, elitekills=careerdetails.EliteKills, monsterkillshardcore=careerdetails.HardcoreMonsterKills,
            highesthardcorelevel=careerdetails.HighestHardcoreLevel, progressionact1=careerdetails.Act1Completed, progressionact2=careerdetails.Act2Completed,
            progressionact3=careerdetails.Act3Completed, progressionact4=careerdetails.Act4Completed, progressionact5=careerdetails.Act5Completed,
            updatedatetime=datetime.now()
            )
        CheckCareer.save()
        #Update each season
    # If In DB async call to API (if update time > threshold) and return DB
    else:
        CheckCareer = models.FactCareer.objects.get(userid=User, seasonid=seasonid)
    return CheckCareer


def UpdateSeason(user, seasondetails):
    return


# Make sure user exists in API
def UpdateUser(battletag, locale):
    DisplayTag = battletag.replace('-', '#')
    # If User doesn't exist yet, insert
    if not models.DimensionUser.objects.filter(battletag=battletag, localeid=locale).exists():
        User = models.DimensionUser(battletag=battletag, battletagdisplay=DisplayTag,
            lastupdated=datetime.now(), localeid=locale)
        User.save()
    # else update lastupdated time to Now
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
    Locale = models.DimensionLocale.objects.get(localenameapi='en_US')
    BattleTag = request.GET.get('battletagcareer')
    User = UpdateUser(BattleTag, Locale)
    CareerDetails = models.FactCareer()
    if not BattleTag:
        #CareerDetails = Career.Career(request.session['CareerProfile'])
        for obj in serializers.deserialize('json', Career.Career(request.session['CareerProfile'])):
            CareerDetails += obj
    else:
        CareerDetails = GetCareer(User.userid, Locale)
        #CareerDetails = DiabloAPI.GetCareer(DiabloAPIConfig.US_SERVER, BattleTag)
        request.session['CareerProfile'] = serializers.serialize('json', [CareerDetails, ])

    HeroPortrait = ""
    CareerTable = ""
    #heroes = CareerDetails.Heroes()
    #for hero in heroes:
    #    HeroPortrait += hero.Portrait
    #    CareerTable += hero.CareerTableRow
    context_instance = {
        'Title': 'Diablo 3',
        'Year': datetime.now().year,
        'UserName': '<li class="menuItem">' + User.battletagdisplay + '</li>',
        'CharacterMenu': HeroPortrait,
        'Act1Completed': GetActProgHTML(CareerDetails.progressionact1),
        'Act2Completed': GetActProgHTML(CareerDetails.progressionact2),
        'Act3Completed': GetActProgHTML(CareerDetails.progressionact3),
        'Act4Completed': GetActProgHTML(CareerDetails.progressionact4),
        'Act5Completed': GetActProgHTML(CareerDetails.progressionact5),
        'BattleTag': re.sub('\#\d{4}', '', User.battletagdisplay),
        'GuildName': '<' + CareerDetails.guildname + '>',
        'CareerTable': CareerTable,
        #'CareerProfile':
            #"\nBattleTag: " + CareerDetails.BattleTag
            #+ "\nParagon Level: " + str(CareerDetails.ParagonLevel)
            #+ "\nSeasonal Paragon Level: " + str(CareerDetails.ParagonLevelSeason)
            #+ "\nElite Kills: " + str(CareerDetails.Kills()['elites'])
            #+ "\nLast Update: " + str(helper.GetUpdateTime(int(CareerDetails.LastUpdated)))
            #+ "\n\nHeroes JSON Dump: " + str(CareerDetails.Heroes())
            #+ "\n\n\nJSON Dump: \n" + str(CareerDetails),
    }
    return render(
        request,
        'career.html',
        context_instance
    )