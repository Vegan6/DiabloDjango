from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
from DiabloDjango.AppCode import DiabloAPI
from DiabloDjango.AppCode.DiabloObjects import Career
from DiabloDjango.AppCode import helper
from DiabloDjango.AppData import models
from DiabloDjango.AppCode.DiabloObjects import Hero
import re
import json
from django.forms.models import model_to_dict
from DiabloDjango.AppCode.helper import GetUpdateTime


HeroPortrait = ""
Heroes = list()
# Step 1 Insert career if not there, pull if it is
# Step 2 Insert career if not there, update & pull if it is (async?)
#On Update Career - Need to Insert/Update Hereoes listed (fallen and alive)
def GetCareer(user, locale):
    global Heroes
    Heroes = list()
    CareerDetails = DiabloAPI.GetCareer(locale.serverurl, user.battletag)
    CurrentCareer = UpdateCareer(user, CareerDetails)
    #Update Seasons
    Seasons = CareerDetails.SeasonalProfiles()
    for season in Seasons:
        CurrentSeason = Career.Career(Seasons[season])
        UpdateSeason(user, CurrentSeason)
    #Update Heroes
    heroes = CareerDetails.Heroes()
    for hero in heroes:
        CurrentHero = Hero.Hero(hero)
        Heroes.append(UpdateHeroFromCareer(user, CurrentHero))    
    return CurrentCareer


def UpdateCareer(user, careerDetails):
    seasonid = -1
    if not models.FactCareer.objects.filter(userid=user, seasonid=seasonid).exists():
        #Still need artisan levels
        CheckCareer = models.FactCareer(
            userid=user, seasonid=seasonid, paragonlevel=careerDetails.ParagonLevel,
            paragonlevelhardcore=careerDetails.ParagonLevelHardcore, paragonlevelseason=careerDetails.ParagonLevelSeason,
            paragonlevelseasonhardcore=careerDetails.ParagonLevelSeasonHardcore, guildname=careerDetails.GuildName,
            lastheroplayed=careerDetails.LastHeroPlayed, lastupdateddatetime=helper.GetUpdateTime(careerDetails.LastUpdated),
            monsterkills=careerDetails.MonsterKills, elitekills=careerDetails.EliteKills, monsterkillshardcore=careerDetails.HardcoreMonsterKills,
            highesthardcorelevel=careerDetails.HighestHardcoreLevel, progressionact1=careerDetails.Act1Completed, progressionact2=careerDetails.Act2Completed,
            progressionact3=careerDetails.Act3Completed, progressionact4=careerDetails.Act4Completed, progressionact5=careerDetails.Act5Completed,
            updatedatetime=datetime.now()
            )
        CheckCareer.save()
        #Update each season
    # If In DB async call to API (if update time > threshold) and return DB
    else:
        CheckCareer = models.FactCareer.objects.get(userid=user, seasonid=seasonid)
    return CheckCareer


def UpdateHeroFromCareer(user, heroDetails):
    global HeroPortrait
    if not models.FactHero.objects.filter(userid=user, apiheroid=heroDetails.HeroId).exists():
        #Still need artisan levels
        Hero = models.FactHero(
            userid=user, apiheroid=heroDetails.HeroId, name=heroDetails.Name, classid=heroDetails.Class, genderid=heroDetails.Gender,
            level=heroDetails.Level, paragonlevel=heroDetails.ParagonLevel, dead=heroDetails.Dead, seasonal=heroDetails.Seasonal,
            hardcore=heroDetails.Hardcore, lastupdateddatetime=GetUpdateTime(heroDetails.LastUpdated), elitekills=heroDetails.EliteKills,
            updatedatetime=datetime.now()
            )
        Hero.save()
    # If In DB async call to API (if update time > threshold) and return DB
    else:
        Hero = models.FactHero.objects.get(userid=user, apiheroid=heroDetails.HeroId)
    
    HeroPortrait += GetHeroMenuItem(Hero, user.battletag)
    
    return Hero

def UpdateSeason(user, seasonDetails):
    seasonid = seasonDetails['seasonId']
    if not models.FactCareer.objects.filter(userid=user, seasonid=seasonid).exists():
        #Still need artisan levels
        CheckCareer = models.FactCareer(
            userid=user, seasonid=seasonid, paragonlevel=seasonDetails.ParagonLevel, paragonlevelhardcore=seasonDetails.ParagonLevelHardcore,             
            monsterkills=seasonDetails.MonsterKills, elitekills=seasonDetails.EliteKills, monsterkillshardcore=seasonDetails.HardcoreMonsterKills,
            highesthardcorelevel=seasonDetails.HighestHardcoreLevel, progressionact1=seasonDetails.Act1Completed, progressionact2=seasonDetails.Act2Completed,
            progressionact3=seasonDetails.Act3Completed, progressionact4=seasonDetails.Act4Completed, progressionact5=seasonDetails.Act5Completed,
            updatedatetime=datetime.now()
            )
        CheckCareer.save()
        #Update each season
    # If In DB async call to API (if update time > threshold) and return DB
    else:
        CheckCareer = models.FactCareer.objects.get(userid=user, seasonid=seasonid)
    return CheckCareer


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
        return '<span class="actprogincomplete">Incomplete</span>'
    
    
def GetHeroMenuItem(hero, battletag):
    LevelType = 'level' if (hero.level < 70) else 'paragon-level'
    DisplayLevel = hero.level if (hero.level < 70) else hero.paragonlevel
    #Return the div for individual hero
    #Need to add a span to distinguish hardcore/dead from not
    if (hero.seasonal):
        nameDisplay = str('<div class="name seasonal">' +
                          '<span class="' + LevelType + '" type="submit" value="Get Hero" name="GetHero" >' +
                          str(DisplayLevel) + '</span>' + str(hero.name) + '</div>' +
                          '<div class="seasonal-true">&nbsp;</div>')
    else:
        nameDisplay = str('<div class="name">' +
                          '<span class="' + LevelType + '" type="submit" value="Get Hero" name="GetHero" >' +
                          str(DisplayLevel) + '</span>' + str(hero.name) + '</div>' +
                          '<div class="seasonal-false">&nbsp;</div>')
        
    return str('<li class="heroMenuItem"><div class="hero clickable" value="' + str(hero.apiheroid) + '">' +
               '<a href="/hero?battletag=' + battletag + '&heroid=' + str(hero.apiheroid) +
               '" class="fill-div">' + '<div class="face ' + hero.classid.externalclassname + '-' +
               hero.genderid.gendername + '">&nbsp;</div>' + nameDisplay + '</a></div></li>')


def career(request):
    """Renders the Career page."""
    assert isinstance(request, HttpRequest)
    Locale = models.DimensionLocale.objects.get(localenameapi='en_US')
    BattleTag = request.GET.get('battletagcareer')
    CareerDetails = models.FactCareer()
    if not BattleTag:
        CareerFromMem = json.loads(request.session['CareerProfile'])
        User = models.DimensionUser.objects.get(userid = CareerFromMem['userid'])
        CareerDetails = GetCareer(User, Locale)
    else:
        User = UpdateUser(BattleTag, Locale)
        CareerDetails = GetCareer(User, Locale)
        toDict = model_to_dict(CareerDetails)
        toJSON = json.dumps(toDict, cls=helper.DateTimeEncoder)
        request.session['CareerProfile'] = toJSON
    
    SeasonDetails = models.FactCareer.objects.filter(userid=User, seasonid__gte=0).order_by('seasonid')
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
        'CareerTable': Heroes,
        'SeasonTable': SeasonDetails,
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