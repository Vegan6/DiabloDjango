from django.shortcuts import render
from django.http import HttpRequest
from DiabloDjango.AppCode import helper
from DiabloDjango.AppCode.DiabloObjects import Hero
from DiabloDjango.AppCode import DiabloAPI
from DiabloDjango.AppData import models
from DiabloDjango.AppCode.Views import View_Career
import json
from django.forms.models import model_to_dict
from datetime import datetime


HeroPortrait = ""
# Step 1 Insert career if not there, pull if it is
# Step 2 Insert career if not there, update & pull if it is (async?)
#On Update Career - Need to Insert/Update Hereoes listed (fallen and alive)
def GetHero(user, locale, heroid):
    global HeroPortrait
    HeroPortrait = ""
    HeroDetails = DiabloAPI.HeroProfile(locale.serverurl, user.battletag, heroid)
    #Update/Get CurrentHero
    CurrentHero = UpdateHero(user, HeroDetails)    
    #Update Hero Portrait List
    Heroes = models.FactHero.objects.filter(userid=user).order_by('seasonal', '-paragonlevel', '-level', '-elitekills')
    for hero in Heroes:
        HeroPortrait += View_Career.GetHeroMenuItem(hero, user.battletag)  
    return CurrentHero


def UpdateHero(user, heroDetails):
    #global HeroPortrait
    if not models.FactHero.objects.filter(userid=user, apiheroid=heroDetails.HeroId).exists():
        #Still need all non career items
        Hero = models.FactHero(
            userid=user, 
            apiheroid=heroDetails.HeroId, 
            name=heroDetails.Name, 
            classid=heroDetails.Class, 
            genderid=heroDetails.Gender,
            level=heroDetails.Level, 
            paragonlevel=heroDetails.ParagonLevel, 
            dead=heroDetails.Dead, 
            seasonal=heroDetails.Seasonal,
            hardcore=heroDetails.Hardcore, 
            lastupdateddatetime=helper.GetUpdateTime(heroDetails.LastUpdated), 
            elitekills=heroDetails.EliteKills,
            monsterkills=heroDetails.MonsterKills,
            seasoncreated=heroDetails.SeasonCreated,
            progressionact1=heroDetails.Act1Completed,
            progressionact2=heroDetails.Act2Completed,
            progressionact3=heroDetails.Act3Completed,
            progressionact4=heroDetails.Act4Completed,
            progressionact5=heroDetails.Act5Completed,
            life=heroDetails.Life,
            damage=heroDetails.Damage,
            toughness=heroDetails.Toughness,
            healing=heroDetails.Healing,
            attackspeed=heroDetails.AttackSpeed,
            armor=heroDetails.Armor,
            strength=heroDetails.Strength,
            dexterity=heroDetails.Dexterity,
            vitality=heroDetails.Vitality,
            intelligence=heroDetails.Intelligence,
            physicalresist=heroDetails.PhysicalResist,
            fireresist=heroDetails.FireResist,
            coldresist=heroDetails.ColdResist,
            lightningresist=heroDetails.LightningResist,
            poisonresist=heroDetails.PoisonResist,
            arcaneresist=heroDetails.ArcaneResist,
            critdamage=heroDetails.CriticalDamage,
            blockchance=heroDetails.BlockChance,
            blockamountmin=heroDetails.BlockAmountMin,
            blockamountmax=heroDetails.BlockAmountMax,
            thorns=heroDetails.Thorns,
            lifesteal=heroDetails.LifeSteal,
            lifeperkill=heroDetails.LifePerKill,
            goldfind=heroDetails.GoldFind,
            magicfind=heroDetails.MagicFind,
            damageincrease=heroDetails.DamageIncrease,
            critchance=heroDetails.CriticalChance,
            damagereduction=heroDetails.DamageReduction,
            lifeonhit=heroDetails.LifeOnHit,
            primaryresource=heroDetails.PrimaryResource,
            secondaryresource=heroDetails.SecondaryResource,
            updatedatetime=datetime.now()
            )
        Hero.save()
    # If In DB async call to API (if update time > threshold) and return DB
    else:
        Hero = models.FactHero.objects.get(userid=user, apiheroid=heroDetails.HeroId)
        Hero.classid=heroDetails.Class
        Hero.genderid=heroDetails.Gender
        Hero.level=heroDetails.Level
        Hero.paragonlevel=heroDetails.ParagonLevel
        Hero.dead=heroDetails.Dead
        Hero.seasonal=heroDetails.Seasonal
        Hero.hardcore=heroDetails.Hardcore
        Hero.lastupdateddatetime=helper.GetUpdateTime(heroDetails.LastUpdated)
        Hero.elitekills=heroDetails.EliteKills
        Hero.monsterkills=heroDetails.MonsterKills
        Hero.seasoncreated=heroDetails.SeasonCreated
        Hero.progressionact1=heroDetails.Act1Completed
        Hero.progressionact2=heroDetails.Act2Completed
        Hero.progressionact3=heroDetails.Act3Completed
        Hero.progressionact4=heroDetails.Act4Completed
        Hero.progressionact5=heroDetails.Act5Completed
        Hero.life=heroDetails.Life
        Hero.damage=heroDetails.Damage
        Hero.toughness=heroDetails.Toughness
        Hero.healing=heroDetails.Healing
        Hero.attackspeed=heroDetails.AttackSpeed
        Hero.armor=heroDetails.Armor
        Hero.strength=heroDetails.Strength
        Hero.dexterity=heroDetails.Dexterity
        Hero.vitality=heroDetails.Vitality
        Hero.intelligence=heroDetails.Intelligence
        Hero.physicalresist=heroDetails.PhysicalResist
        Hero.fireresist=heroDetails.FireResist
        Hero.coldresist=heroDetails.ColdResist
        Hero.lightningresist=heroDetails.LightningResist
        Hero.poisonresist=heroDetails.PoisonResist
        Hero.arcaneresist=heroDetails.ArcaneResist
        Hero.critdamage=heroDetails.CriticalDamage
        Hero.blockchance=heroDetails.BlockChance
        Hero.blockamountmin=heroDetails.BlockAmountMin
        Hero.blockamountmax=heroDetails.BlockAmountMax
        Hero.thorns=heroDetails.Thorns
        Hero.lifesteal=heroDetails.LifeSteal
        Hero.lifeperkill=heroDetails.LifePerKill
        Hero.goldfind=heroDetails.GoldFind
        Hero.magicfind=heroDetails.MagicFind
        Hero.damageincrease=heroDetails.DamageIncrease
        Hero.critchance=heroDetails.CriticalChance
        Hero.damagereduction=heroDetails.DamageReduction
        Hero.lifeonhit=heroDetails.LifeOnHit
        Hero.primaryresource=heroDetails.PrimaryResource
        Hero.secondaryresource=heroDetails.SecondaryResource
        Hero.updatedatetime=datetime.now()
        Hero.save()
    return Hero


def hero(request):
    """Renders the hero page."""
    assert isinstance(request, HttpRequest)
    HeroID = request.GET.get('heroid', '')
    Locale = models.DimensionLocale.objects.get(localenameapi='en_US')
    BattleTag = request.GET.get('battletag')
    User = View_Career.UpdateUser(BattleTag, Locale)
    if not models.FactCareer.objects.filter(userid=User, seasonid=-1).exists():
        raise Exception('Ooops Error:\n' + 'Career Does Not Exist.')
    else:
        CareerDetails = models.FactCareer.objects.get(userid=User, seasonid=-1)
    # If HeroID not passed in use current hero or last played hero
    if not HeroID:
        HeroID = json.loads(request.session['CurrentHero'])['apiheroid']
        if not HeroID:
            HeroID = int(CareerDetails.lastheroplayed)
    else:
        HeroID = int(HeroID)
    CurrentHero = GetHero(User, Locale, HeroID)
        
    #Save Current Hero to Cookies
    toDict = model_to_dict(CurrentHero)
    toJSON = json.dumps(toDict, cls=helper.DateTimeEncoder)
    request.session['CurrentHero'] = toJSON

    context_instance = {
        'Title': 'Diablo 3',
        'Year': datetime.now().year,
        'UserName': '<li class="menuItem">' + User.battletagdisplay + '</li>',
        #'Damage': "{:,}".format(CurrentHero.damage),
        'HeroName': CurrentHero.name,
        'CharacterMenu': HeroPortrait,
#         'HeroVitru': CurrentHero.BackImage,
#         'HandsIcon': CurrentHero.Hands.IconURL,
#         'HandsToolTip': CurrentHero.Hands.ToolTipURL,
#         'ChestIcon': CurrentHero.Chest.IconURL,
#         'ChestToolTip': CurrentHero.Chest.ToolTipURL,
#         'LegsIcon': CurrentHero.Legs.IconURL,
#         'LegsToolTip': CurrentHero.Legs.ToolTipURL,

        'AttackStats': '<div><span>Damage</span><span>' + "{:,}".format(CurrentHero.damage) + '</span></div>'
            + '<div><span>Critical Hit Chance</span><span>' + str(CurrentHero.critchance) + "%" + '</span></div>'
            + '<div><span>Critical Hit Damage</span><span>' + str(CurrentHero.critdamage) + "%" + '</span></div>'
            + '<div><span>Attack Speed</span><span>' + str(CurrentHero.attackspeed) + '</span></div>',
 
        'LifeStats': '<div><span>Life</span><span>' + "{:,}".format(CurrentHero.life) + '</span></div>'
            + '<div><span>Life On Hit</span><span>' + "{:,}".format(CurrentHero.lifeonhit) + '</span></div>'
            + '<div><span>Toughness</span><span>' + "{:,}".format(CurrentHero.toughness) + '</span></div>'
            + '<div><span>Healing</span><span>' + "{:,}".format(CurrentHero.healing) + '</span></div>'
            + '<div><span>Armor</span><span>' + "{:,}".format(CurrentHero.armor) + '</span></div>',
 
        'ResistanceStats': '<div><span>Cold</span><span>' + "{:,}".format(CurrentHero.coldresist) + '</span></div>'
            + '<div><span>Fire</span><span>' + "{:,}".format(CurrentHero.fireresist) + '</span></div>'
            + '<div><span>Physical</span><span>' + "{:,}".format(CurrentHero.physicalresist) + '</span></div>'
            + '<div><span>Arcane</span><span>' + "{:,}".format(CurrentHero.arcaneresist) + '</span></div>',
 
        'BuffStats': '<div><span>Magic Find Percent</span><span>' + "{:,}".format(CurrentHero.magicfind) + '%</span></div>'
            + '<div><span>Gold Find Percent</span><span>' + "{:,}".format(CurrentHero.goldfind) + '%</span></div>'
            + '<div><span>Life Steal</span><span>' + "{:,}".format(CurrentHero.lifesteal) + '</span></div>'
            + '<div><span>Damage Increase</span><span>' + "{:,}".format(CurrentHero.damageincrease) + '</span></div>'
            + '<div><span>Damage Reduction</span><span>' + "{:,}".format(CurrentHero.damagereduction) + '</span></div>',
# 
#         'StatList': CurrentHero.statList,

        'HeroProfile':
            "\nHero Name: " + CurrentHero.name
            + "\nParagon Level: " + str(CurrentHero.paragonlevel)
            + "\nClass: " + CurrentHero.classid.classname
            + "\nGender: " + CurrentHero.genderid.gendername
#             + "\nCritical Hit Chance: " + str(CurrentHero.critchance) + "%"
#             + "\nCritical Hit Damage: " + str(CurrentHero.critdamage) + "%"
            + "\nLast Update: " + str(CurrentHero.lastupdateddatetime),
#             + "\nDamage: " + str(CurrentHero.damage),
    }

    return render(
        request,
        'hero.html',
        context_instance
    )