from django.shortcuts import render
from django.http import HttpRequest
from DiabloDjango.AppCode import helper
from DiabloDjango.AppCode.DiabloObjects import Hero
from DiabloDjango.AppCode import DiabloAPI
from DiabloDjango.AppData import models
from DiabloDjango.AppCode.Views import View_Career
import json
from django.forms.models import model_to_dict
from datetime import datetime, timedelta


HeroPortrait = ""
# Step 1 Insert career if not there, pull if it is
# Step 2 Insert career if not there, update & pull if it is (async?)
#On Update Career - Need to Insert/Update Hereoes listed (fallen and alive)
def GetHero(user, locale, heroid):
    global HeroPortrait
    HeroPortrait = ""
    #Update/Get CurrentHero
    if not models.FactHero.objects.filter(userid=user, apiheroid=heroid).exists():
        HeroDetails = DiabloAPI.HeroProfile(locale.serverurl, user.battletag, heroid)
        #Still need Skills, items, etc
        Hero = models.FactHero(
            userid=user, 
            apiheroid=HeroDetails.HeroId, 
            name=HeroDetails.Name, 
            classid=HeroDetails.Class, 
            genderid=HeroDetails.Gender,
            level=HeroDetails.Level, 
            paragonlevel=HeroDetails.ParagonLevel, 
            dead=HeroDetails.Dead, 
            seasonal=HeroDetails.Seasonal,
            hardcore=HeroDetails.Hardcore, 
            lastupdateddatetime=helper.GetUpdateTime(HeroDetails.LastUpdated), 
            elitekills=HeroDetails.EliteKills,
            monsterkills=HeroDetails.MonsterKills,
            seasoncreated=HeroDetails.SeasonCreated,
            progressionact1=HeroDetails.Act1Completed,
            progressionact2=HeroDetails.Act2Completed,
            progressionact3=HeroDetails.Act3Completed,
            progressionact4=HeroDetails.Act4Completed,
            progressionact5=HeroDetails.Act5Completed,
            life=HeroDetails.Life,
            damage=HeroDetails.Damage,
            toughness=HeroDetails.Toughness,
            healing=HeroDetails.Healing,
            attackspeed=HeroDetails.AttackSpeed,
            armor=HeroDetails.Armor,
            strength=HeroDetails.Strength,
            dexterity=HeroDetails.Dexterity,
            vitality=HeroDetails.Vitality,
            intelligence=HeroDetails.Intelligence,
            physicalresist=HeroDetails.PhysicalResist,
            fireresist=HeroDetails.FireResist,
            coldresist=HeroDetails.ColdResist,
            lightningresist=HeroDetails.LightningResist,
            poisonresist=HeroDetails.PoisonResist,
            arcaneresist=HeroDetails.ArcaneResist,
            critdamage=HeroDetails.CriticalDamage,
            blockchance=HeroDetails.BlockChance,
            blockamountmin=HeroDetails.BlockAmountMin,
            blockamountmax=HeroDetails.BlockAmountMax,
            thorns=HeroDetails.Thorns,
            lifesteal=HeroDetails.LifeSteal,
            lifeperkill=HeroDetails.LifePerKill,
            goldfind=HeroDetails.GoldFind,
            magicfind=HeroDetails.MagicFind,
            damageincrease=HeroDetails.DamageIncrease,
            critchance=HeroDetails.CriticalChance,
            damagereduction=HeroDetails.DamageReduction,
            lifeonhit=HeroDetails.LifeOnHit,
            primaryresource=HeroDetails.PrimaryResource,
            secondaryresource=HeroDetails.SecondaryResource,
            updatedatetime=datetime.now()
            )
        Hero.save()
    # If In DB async call to API (if update time > threshold) and return DB
    else:
        Hero = models.FactHero.objects.get(userid=user, apiheroid=heroid)
        if Hero.updatedatetime <= datetime.now() - timedelta(hours=1):
            HeroDetails = DiabloAPI.HeroProfile(locale.serverurl, user.battletag, heroid)
            Hero.classid=HeroDetails.Class
            Hero.genderid=HeroDetails.Gender
            Hero.level=HeroDetails.Level
            Hero.paragonlevel=HeroDetails.ParagonLevel
            Hero.dead=HeroDetails.Dead
            Hero.seasonal=HeroDetails.Seasonal
            Hero.hardcore=HeroDetails.Hardcore
            Hero.lastupdateddatetime=helper.GetUpdateTime(HeroDetails.LastUpdated)
            Hero.elitekills=HeroDetails.EliteKills
            Hero.monsterkills=HeroDetails.MonsterKills
            Hero.seasoncreated=HeroDetails.SeasonCreated
            Hero.progressionact1=HeroDetails.Act1Completed
            Hero.progressionact2=HeroDetails.Act2Completed
            Hero.progressionact3=HeroDetails.Act3Completed
            Hero.progressionact4=HeroDetails.Act4Completed
            Hero.progressionact5=HeroDetails.Act5Completed
            Hero.life=HeroDetails.Life
            Hero.damage=HeroDetails.Damage
            Hero.toughness=HeroDetails.Toughness
            Hero.healing=HeroDetails.Healing
            Hero.attackspeed=HeroDetails.AttackSpeed
            Hero.armor=HeroDetails.Armor
            Hero.strength=HeroDetails.Strength
            Hero.dexterity=HeroDetails.Dexterity
            Hero.vitality=HeroDetails.Vitality
            Hero.intelligence=HeroDetails.Intelligence
            Hero.physicalresist=HeroDetails.PhysicalResist
            Hero.fireresist=HeroDetails.FireResist
            Hero.coldresist=HeroDetails.ColdResist
            Hero.lightningresist=HeroDetails.LightningResist
            Hero.poisonresist=HeroDetails.PoisonResist
            Hero.arcaneresist=HeroDetails.ArcaneResist
            Hero.critdamage=HeroDetails.CriticalDamage
            Hero.blockchance=HeroDetails.BlockChance
            Hero.blockamountmin=HeroDetails.BlockAmountMin
            Hero.blockamountmax=HeroDetails.BlockAmountMax
            Hero.thorns=HeroDetails.Thorns
            Hero.lifesteal=HeroDetails.LifeSteal
            Hero.lifeperkill=HeroDetails.LifePerKill
            Hero.goldfind=HeroDetails.GoldFind
            Hero.magicfind=HeroDetails.MagicFind
            Hero.damageincrease=HeroDetails.DamageIncrease
            Hero.critchance=HeroDetails.CriticalChance
            Hero.damagereduction=HeroDetails.DamageReduction
            Hero.lifeonhit=HeroDetails.LifeOnHit
            Hero.primaryresource=HeroDetails.PrimaryResource
            Hero.secondaryresource=HeroDetails.SecondaryResource
            Hero.updatedatetime=datetime.now()
            Hero.save()
    #Update Hero Portrait List
    Heroes = models.FactHero.objects.filter(userid=user).order_by('seasonal', '-paragonlevel', '-level', '-elitekills')
    for hero in Heroes:
        HeroPortrait += View_Career.GetHeroMenuItem(hero, user.battletag)  
    return Hero

def GetBackImage(hero):
    if (hero.genderid.genderid == 0):
        backImage = 'VitruvianMan.jpg'
    else:
        backImage = 'VitruvianWoman.jpg'
    return str(backImage)

def hero(request):
    """Renders the hero page."""
    assert isinstance(request, HttpRequest)
    #HeroID = request.GET.get('heroid', '')
    Locale = models.DimensionLocale.objects.get(localenameapi='en_US')
    BattleTag = request.session['battletag']
    User = View_Career.UpdateUser(BattleTag, Locale)
    HeroID = None
    if request.method == 'POST':
        HeroID = request.POST['heroid']  
    # If HeroID not passed in use current hero or last played hero
    if not HeroID:
        HeroID = json.loads(request.session['CurrentHero'])['apiheroid']
        if not HeroID:
            if not models.FactCareer.objects.filter(userid=User, seasonid=-1).exists():
                raise Exception('Ooops Error:\n' + 'Career Does Not Exist.')
            else:
                CareerDetails = models.FactCareer.objects.get(userid=User, seasonid=-1)
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
        'Damage': "{:,}".format(CurrentHero.damage),
        'HeroName': CurrentHero.name,
        'CharacterMenu': HeroPortrait,
        'HeroVitru': GetBackImage(CurrentHero),
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
             + "\nCritical Hit Chance: " + str(CurrentHero.critchance) + "%"
             + "\nCritical Hit Damage: " + str(CurrentHero.critdamage) + "%"
            + "\nLast Update: " + str(CurrentHero.lastupdateddatetime),
#             + "\nDamage: " + str(CurrentHero.damage),
    }

    return render(
        request,
        'hero.html',
        context_instance
    )