from DiabloDjango.AppCode import DiabloAPI
from . import DiabloAPIConfig


class Career(dict):
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
                heroProfiles.append(DiabloAPI.HeroProfile(DiabloAPIConfig.CURRENTSERVER, self.BattleTagURI, int(hero['id'])))
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