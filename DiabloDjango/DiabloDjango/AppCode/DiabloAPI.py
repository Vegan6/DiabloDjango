import requests
import json
from decimal import Decimal

# Static Variables
EU_SERVER = 'https://eu.api.battle.net'
US_SERVER = 'https://us.api.battle.net'
ASIA_SERVER = 'https://as.api.battle.net'

EN_LOCALE = 'locale=en_US'

# Heretic Key
API_KEY = 'apikey=wszpeaq9nkmskx58ra68yknst4dage85'

ICON_URL = 'http://media.blizzard.com/d3/icons/items/large/<ITEM>.png'
#TOOLTIP_URL = '<SERVER>/d3/data/<TOOLTIP>?' + EN_LOCALE + '&' + API_KEY
TOOLTIP_URL = 'https://us.battle.net/d3/en/<ITEM>'

BATTLETAG = ''
CURRENTSERVER = ''

#Icon
#http://media.blizzard.com/d3/icons/items/small/unique_gloves_set_13_x1_demonhunter_male.png
#http://media.blizzard.com/d3/icons/items/large/<itemname>.png
#Tooltip
#https://us.api.battle.net/d3/data/item/CkUIlaL0zggSBwgEFVyXwXod89VHtB1yjh0hHTp12owdmKeOwB1-
#VrMuHfNwB60wi1I4lQJAAFASWARglQKAAUa1AclbkqQYuN2MrA9QBFgCoAG43YysDw?locale=en_US&apikey=wszpeaq9nkmskx58ra68yknst4dage85
#https://us.api.battle.net/d3/data/<tooltip params>


genders = {0: 'Male', 1: 'Female'}
classes = {
    'demon-hunter': 'Demon Hunter',
    'crusader': 'Crusader',
    'barbarian': 'Barbarian',
    'monk': 'Monk',
    'witch-doctor': 'Witch Doctor',
    'wizard': 'Wizard'
}

# Load Career
# Returns Career Class


def GetCareer(Host, BattleTag):
    global BATTLETAG, CURRENTSERVER
    CURRENTSERVER = Host
    BATTLETAG = BattleTag
    url = "%s/d3/profile/%s/?%s&%s" % (CURRENTSERVER, BATTLETAG, EN_LOCALE, API_KEY)
    response = requests.get(url)
    response
    if response.status_code == 200:
        return Career(json.loads(response.text))
    else:
        raise Exception('Error:\n' + response.text)


class Career(dict):
    global CURRENTSERVER

    # Create Career Object
    def Kills(self):
        return self['kills']

    def Heroes(self):
        #set this to return Hero Object
        #heroes = dict()
        heroProfiles = list()
        if len(self['heroes']) > 0:
            for hero in self['heroes']:
                #heroes[hero['id']] = hero['name']
                heroProfiles.append(HeroProfile(CURRENTSERVER, self.BattleTagURI, int(hero['id'])))
        #return heroes
        return heroProfiles

    def TimePlayed(self):
        return self['timePlayed']

    def Progression(self):
        return self['progression']

    @property
    def BattleTag(self):
        return self['battleTag']

    @property
    def BattleTagURI(self):
        return str(self['battleTag']).replace("#", "-")

    @property
    def BattleTagDisplay(self):
        return '<li class="menuItem">' + str(self['battleTag']).replace("#", "-") + '</li>'

    @property
    def ParagonLevel(self):
        return self['paragonLevel']

    @property
    def ParagonLevelSeason(self):
        return self['paragonLevelSeason']

    @property
    def LastHeroPlayed(self):
        return self['lastHeroPlayed']

    @property
    def LastUpdated(self):
        return int(self['lastUpdated'])


def HeroProfile(Host, BattleTag, HeroId):
    # Load Hero Profile
    # Returns Hero Class
    url = "%s/d3/profile/%s/hero/%s?%s&%s" % (Host, BattleTag, HeroId, EN_LOCALE, API_KEY)
    response = requests.get(url)
    if response.status_code == 200:
        return Hero(json.loads(response.text))
    else:
        raise Exception('Error:\n' + response.text)


class Hero(dict):
    # Create Hero Object
    def ActiveSkillsDictionary(self):
        skills = self['skills']
        return skills['active']

    def PassiveSkillsDictionary(self):
        skills = self['skills']
        return skills['passive']

    def Stats(self):
        return self['stats']

    def Items(self):
        return self['items']

    # Create Item Properties
    @property
    def Hands(self):
        return Item(self.Items()['hands'])

    @property
    def Chest(self):
        return Item(self.Items()['torso'])

    @property
    def Legs(self):
        return Item(self.Items()['legs'])

    # Create Hero Properties
    @property
    def statList(self):
        return self.Stats()

    @property
    def ArcaneResist(self):
        return int(self.Stats()['arcaneResist'])

    @property
    def Armor(self):
        return int(self.Stats()['armor'])

    @property
    def AttackSpeed(self):
        return round(Decimal(self.Stats()['attackSpeed']), 2)

    @property
    def BackImage(self):
        if (int(self['gender']) == 0):
            backImage = 'VitruvianMan.jpg'
        else:
            backImage = 'VitruvianWoman.jpg'
        return str(backImage)

    @property
    def ColdResist(self):
        return int(self.Stats()['coldResist'])

    @property
    def CriticalDamage(self):
        return int(self.Stats()['critDamage'] * 100)

    @property
    def CriticalChance(self):
        return int(self.Stats()['critChance'] * 100)

    @property
    def Class(self):
        classId = str(self['class'])
        return classes[classId]

    @property
    def Damage(self):
        return int(self.Stats()['damage'])

    @property
    def DamageIncrease(self):
        return int(self.Stats()['damageIncrease'] * 100)

    @property
    def DamageReduction(self):
        return int(self.Stats()['damageReduction'] * 100)

    @property
    def DisplayLevel(self):
        if (self.Level < 70):
            return self.Level
        else:
            return self.ParagonLevel

    @property
    def FireResist(self):
        return int(self.Stats()['fireResist'])

    @property
    def Gender(self):
        genderId = int(self['gender'])
        return genders[genderId]

    @property
    def GoldFind(self):
        return int(self.Stats()['goldFind'] * 100)

    @property
    def Healing(self):
        return int(self.Stats()['healing'])

    @property
    def HeroId(self):
        return self['id']

    @property
    def LastUpdated(self):
        return int(self['last-updated'])

    @property
    def Level(self):
        return int(self['level'])

    @property
    def Life(self):
        return int(self.Stats()['life'])

    @property
    def LifeOnHit(self):
        return int(self.Stats()['lifeOnHit'])

    @property
    def LifeSteal(self):
        return int(self.Stats()['lifeSteal'])

    @property
    def MagicFind(self):
        return int(self.Stats()['magicFind'] * 100)

    @property
    def Name(self):
        return self['name']

    @property
    def ParagonLevel(self):
        return self['paragonLevel']

    @property
    def PhysicalResist(self):
        return int(self.Stats()['physicalResist'])

    @property
    def PoisonResist(self):
        return int(self.Stats()['poisonResist'])

    @property
    def Portrait(self):
        LevelType = 'level' if (self.Level < 70) else 'paragon-level'
        #Return the div for individual hero
        #Need to add a span to distinguish paragon from standard
        if (self['seasonal']):
            nameDisplay = str('<div class="name seasonal">' +
            '<span class="' + LevelType + '" type="submit" value="Get Hero" name="GetHero" >' +
                str(self.DisplayLevel) + '</span>' + str(self.Name) + '</div>' +
            '<div class="seasonal-true">&nbsp;</div>')
        else:
            nameDisplay = str('<div class="name">' +
            '<span class="' + LevelType + '" type="submit" value="Get Hero" name="GetHero" >' +
                str(self.DisplayLevel) + '</span>' + str(self.Name) + '</div>' +
            '<div class="seasonal-false">&nbsp;</div>')

        return str('<li class="heroMenuItem"><div class="hero clickable" value="' + str(self['id']) + '">' +
                    '<a href="/hero?battletag=' + BATTLETAG + '&heroid=' + str(self.HeroId) + '" class="fill-div">' +
                    '<div class="face ' + self['class'] + '-' + self.Gender + '">&nbsp;</div>' + nameDisplay + '</a></div></li>')

    @property
    def Toughness(self):
        return int(self.Stats()['toughness'])


class Item(dict):
    global ICON_URL, TOOLTIP_URL
    iconURL = ICON_URL
    toolTipURL = TOOLTIP_URL

    @property
    def IconURL(self):
        return self.iconURL.replace("<ITEM>", str(self['icon']))

    @property
    def ToolTipURL(self):
        return self.toolTipURL.replace("<ITEM>", str(self['tooltipParams']))

    @property
    def DisplayColor(self):
        return self['displayColor']

    @property
    def Name(self):
        return self['name']

    @property
    def ID(self):
        return self['id']

    @property
    def SetItemsEquipped(self):
        return self['setItemsEquipped']
