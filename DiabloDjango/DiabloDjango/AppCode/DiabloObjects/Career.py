import logging
import re
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
                heroProfiles.append(DiabloAPI.HeroProfile(DiabloAPIConfig.CURRENTSERVER, self.BattleTagURI, int(hero['id'])))
                    
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
    def Act1Completed(self):
        progression = self['progression']
        act1 = progression['act1']
        if (act1):
            return '<span class="actprogcomplete">Completed</span>'
        else:
            return '<span class="actprogincomplete">Incomplet</span>'

    @property
    def Act2Completed(self):
        progression = self['progression']
        act2 = progression['act2']
        if (act2):
            return '<span class="actprogcomplete">Completed</span>'
        else:
            return '<span class="actprogincomplete">Incomplet</span>'

    @property
    def Act3Completed(self):
        progression = self['progression']
        act3 = progression['act3']
        if (act3):
            return '<span class="actprogcomplete">Completed</span>'
        else:
            return '<span class="actprogincomplete">Incomplet</span>'

    @property
    def Act4Completed(self):
        progression = self['progression']
        act4 = progression['act4']
        if (act4):
            return '<span class="actprogcomplete">Completed</span>'
        else:
            return '<span class="actprogincomplete">Incomplet</span>'

    @property
    def Act5Completed(self):
        progression = self['progression']
        act5 = progression['act5']
        if (act5):
            return '<span class="actprogcomplete">Completed</span>'
        else:
            return '<span class="actprogincomplete">Incomplet</span>'

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
    def GuildName(self):
        return ' <' + self['guildName'] + '>'

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

    @property
    def UserName(self):
        return re.sub('\#\d{4}', '', str(self['battleTag']))