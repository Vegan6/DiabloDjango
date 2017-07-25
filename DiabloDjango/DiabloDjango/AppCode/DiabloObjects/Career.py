import logging
import re


class Career(dict):
    # Create Career Object
    def Kills(self):
        return self['kills']

    def Heroes(self):
        return self['heroes']

    def SeasonalProfiles(self):
        return self['seasonalProfiles']

    def TimePlayed(self):
        return self['timePlayed']

    def Progression(self):
        return self['progression']

    def log(self, text):
        logging.basicConfig(filename="py_log.txt", level=logging.ERROR)
        logging.info("!!!Problem:" + text)

    @property
    def Act1Completed(self):
        progression = self['progression']
        act1 = progression['act1']
        return act1

    @property
    def Act2Completed(self):
        progression = self['progression']
        act2 = progression['act2']
        return act2

    @property
    def Act3Completed(self):
        progression = self['progression']
        act3 = progression['act3']
        return act3

    @property
    def Act4Completed(self):
        progression = self['progression']
        act4 = progression['act4']
        return act4

    @property
    def Act5Completed(self):
        progression = self['progression']
        act5 = progression['act5']
        return act5

    @property
    def BattleTag(self):
        return self['battleTag']

    @property
    def BattleTagURI(self):
        return str(self['battleTag']).replace("#", "-")

    @property
    def BattleTagDisplay(self):
        return '<li class="menuItem">' + str(self['battleTag']) + '</li>'
    
    @property
    def BlacksmithLevel(self):
        return (self['blacksmith'])['level']

    @property
    def EliteKills(self):
        return int(self.Kills()['elites'])

    @property
    def GuildName(self):
        return self['guildName']

    @property
    def HardcoreMonsterKills(self):
        return int(self.Kills()['hardcoreMonsters'])

    @property
    def HighestHardcoreLevel(self):
        return self['highestHardcoreLevel']

    @property
    def MonsterKills(self):
        return int(self.Kills()['monsters'])

    @property
    def ParagonLevel(self):
        return self['paragonLevel']

    @property
    def ParagonLevelHardcore(self):
        return self['paragonLevelHardcore']

    @property
    def ParagonLevelSeason(self):
        return self['paragonLevelSeason']

    @property
    def ParagonLevelSeasonHardcore(self):
        return self['paragonLevelSeasonHardcore']

    @property
    def LastHeroPlayed(self):
        return self['lastHeroPlayed']

    @property
    def LastUpdated(self):
        return int(self['lastUpdated'])

    @property
    def UserName(self):
        return re.sub('\#\d{4}', '', str(self['battleTag']))