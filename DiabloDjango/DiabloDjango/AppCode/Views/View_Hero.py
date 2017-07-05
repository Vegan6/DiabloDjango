from django.shortcuts import render
from django.http import HttpRequest
from DiabloDjango.AppCode.helper import *
from DiabloDjango.AppCode.DiabloObjects import Career
from DiabloDjango.AppCode.DiabloObjects import Hero


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