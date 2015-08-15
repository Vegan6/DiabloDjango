import requests
import json

# Static Variables
EU_SERVER = 'https://eu.api.battle.net'
US_SERVER = 'https://us.api.battle.net'
ASIA_SERVER = 'https://as.api.battle.net'

EN_LOCALE = 'locale=en_US'

# Heretic Key
API_KEY = 'apikey=wszpeaq9nkmskx58ra68yknst4dage85'

genders = {0: 'Male', 1: 'Female'}
classes = {
    'demon-hunter': 'Demon Hunter',
    'crusader': 'Crusader',
    'barbarian': 'Barbarian',
    'monk': 'Monk',
    'witch-doctor':
    'Witch Doctor',
    'wizard': 'Wizard'
}


# Load Career
# Returns Career Class


def GetCareer(Host, BattleTag):
    url = "%s/d3/profile/%s/?%s&%s" % (Host, BattleTag, EN_LOCALE, API_KEY)
    response = requests.get(url)
    if response.status_code == 200:
        return Career(json.loads(response.text))
    else:
        raise Exception('Error:\n' + response.text)


class Career(dict):
    Host = US_SERVER

    # Create Career Object
    def Kills(self):
        return self['kills']

    def Heroes(self):
        #set this to return Hero Object
        global US_SERVER
        #heroes = dict()
        heroProfiles = list()
        #for hero in self['heroes']:
            #heroes[hero['id']] = hero['name']
            #heroProfiles.append(HeroProfile(Career.Host, self['battleTag'], hero['id']))
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

    @property
    def ParagonLevel(self):
        return self['paragonLevel']

    @property
    def Gender(self):
        genderId = int(self['gender'])
        return genders[genderId]

    @property
    def Class(self):
        classId = str(self['class'])
        return classes[classId]

    @property
    def LastUpdated(self):
        return int(self['last-updated'])

    @property
    def Level(self):
        return int(self['level'])

    @property
    def DisplayLevel(self):
        if (self.Level > self.ParagonLevel):
            return self.Level
        else:
            return self.ParagonLevel

    @property
    def Name(self):
        return self['name']

    @property
    def Portrait(self):
        #Return the div for individual hero
        if (self['seasonal'] == 'true'):
            nameDisplay = str('<div class="name seasonal">' +
            '<span class="level">' + str(self.DisplayLevel) + '</span>' + str(self.Name) + '</div>' +
            '<div class="seasonal-true">&nbsp;</div>')
        else:
            nameDisplay = str('<div class="name">' +
            '<span class="level">' + str(self.DisplayLevel) + '</span>' + str(self.Name) + '</div>' +
            '<div class="seasonal-false">&nbsp;</div>')

        return str('<div class="hero clickable" data-id="' + str(self['id']) + '">' +
                    '<div class="face ' + self['class'] + '-' + self.Gender + '">&nbsp;</div>' +
                    nameDisplay +
                '</div>')