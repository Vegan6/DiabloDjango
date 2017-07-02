import logging
from DiabloDjango.AppCode import *
from DiabloDjango.AppCode import DiabloAPI
from . import DiabloAPIConfig


class Career(dict):
    # Create Career Object
    def Kills(self):
        return self['kills']

    def Heroes(self):
        #set this to return Hero Object
        #heroes = dict()
        global DiabloAPI
        heroProfiles = list()
        if len(self['heroes']) > 0:
            for hero in self['heroes']:
                try:
                    heroProfiles.append(DiabloAPI.HeroProfile(DiabloAPIConfig.CURRENTSERVER, self.BattleTagURI, int(hero['id'])))
                except Exception as excp:
                    self.log(excp)
                except:
                    self.log("Unexpected error:", sys.exc_info()[0])
        #return heroes
        return heroProfiles

    def TimePlayed(self):
        return self['timePlayed']

    def Progression(self):
        return self['progression']

    def log(text):
        logging.basicConfig(filename="py_log.txt", level=logging.ERROR)
        logging.info("!!!Problem:" + text)

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