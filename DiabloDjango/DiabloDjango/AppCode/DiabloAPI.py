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
classes = {'demon-hunter': 'Demon Hunter', 'crusader': 'Crusader', 'barbarian': 'Barbarian', 'monk': 'Monk', 'witch-doctor': 'Witch Doctor', 'wizard': 'Wizard'}


# Load Career
# Returns Career Class


def GetCareer(Host, BattleTag):
    url = "%s/d3/profile/%s/?%s&%s" % (Host, BattleTag, EN_LOCALE, API_KEY)
    response = requests.get(url)
    if response.status_code == 200:
        return Career(json.loads(response.text))
    else:
        raise Exception('Error:\n' + response.text)


# Create Career Object


class Career(dict):
    
    def Kills(self):
        return self['kills']

    def Heroes(self):
        #set this to return Hero Object
        heroes = dict()
        heroProfiles = list()
        for hero in self['heroes']:
            heroes[hero['id']] = hero['name']
            #heroProfiles.append(HeroProfile(Host, self['battleTag'], hero['id']))
        return heroes
        #return heroProfiles

    def TimePlayed(self):
        return self['timePlayed']

    def Progression(self):
        return self['progression']


# Load Hero Profile
# Returns Hero Class


def HeroProfile(Host, BattleTag, HeroId):
    url = "%s/d3/profile/%s/hero/%s?%s&%s" % (Host, BattleTag, HeroId, EN_LOCALE, API_KEY)
    response = requests.get(url)
    if response.status_code == 200:
        return Hero(json.loads(response.text))
    else:
        raise Exception('Error:\n' + response.text)


# Create Hero Object


class Hero(dict):

    def ActiveSkillsDictionary(self):
        skills = self['skills']
        return skills['active']

    def PassiveSkillsDictionary(self):
        skills = self['skills']
        return skills['passive']

    def Gender(self):
        genderId = int(self['gender'])
        return genders[genderId]

    def Class(self):
        classId = str(self['class'])
        return classes[classId]