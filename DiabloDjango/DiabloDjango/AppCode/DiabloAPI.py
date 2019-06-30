import requests
import json
import logging
#import os.path
from .DiabloObjects import DiabloAPIConfig
from .DiabloObjects import Hero
from .DiabloObjects import Career
from .DiabloObjects import Leaderboard
from DiabloDjango.AppData import models

# Load Career
# Returns Career Class


def GetCareer(Host, BattleTag):
    DiabloAPIConfig.CURRENTSERVER = Host
    DiabloAPIConfig.BATTLETAG = BattleTag
    url = "%s/d3/profile/%s/?%s&%s" % (Host, BattleTag, DiabloAPIConfig.EN_LOCALE, DiabloAPIConfig.API_KEY)
    #url = "https://us.api.blizzard.com/d3/profile/Heretic-1984/?locale=en_US&access_token=USKLUsusrWy9xBoKj4vaK4onV9E2YBRvY7"
    response = requests.get(url)
    response
    if response.status_code == 200:
        # log(response.text)
        if response.text[0] and response.text[0] != 'REQUEST_TIMEOUT':
            return Career.Career(json.loads(response.text))
        else:
            raise Exception('Ooops Error:\n' + response.text)
    else:
        raise Exception('Error:\n' + response.text)


def HeroProfile(Host, BattleTag, HeroId):
    # Load Hero Profile
    # Returns Hero Class
    url = "%s/d3/profile/%s/hero/%s?%s&%s" % (Host, BattleTag, HeroId, DiabloAPIConfig.EN_LOCALE, DiabloAPIConfig.API_KEY)
    response = requests.get(url)
    if response.status_code == 200:
        return Hero.Hero(json.loads(response.text))
    else:
        raise Exception('Error:\n' + response.text)

#Leaderboard URL
#https://us.api.battle.net/data/d3/season/6/leaderboard/rift-team-4
def AuthToken():
    url = 'http://us.api.blizzard.com/oauth/token'
    #secret = models.DimensionConfig.objects.get(ConfigName='APISecret')
    #apikey = models.DimensionConfig.objects.get(ConfigName='APIKey')
    secret = 'x3uTTXHjbDRWSmAmENCm4mdbza8xaaun'
    apikey = 'wszpeaq9nkmskx58ra68yknst4dage85'
    header = { 'Authorization': 'Basic Base64(%s:%s)' % (apikey, secret) }
    data = {' grant_type': 'client_credentials', 'client_id' : apikey, 'client_secret' : secret }
    #response = requests.post(url, data=json.dumps(data), headers=header)
    #if response.status_code == 200:
    return 'USKLUsusrWy9xBoKj4vaK4onV9E2YBRvY7'
        #return response.text
    #else:
        #raise Exception('Error:\n' + response.text)

def GetLeaderboards(token, data_point, season):
    url = 'https://us.api.blizzard.com/data/d3/season/%s/leaderboard/%s?access_token=%s' % (season, data_point, token)
    response = requests.get(url)
    return Leaderboard.Leaderboard(json.loads(response.text))

def log(text):
    logging.basicConfig(filename="py_log.txt", level=logging.DEBUG)
    #logger = logging.getLogger()
    #logger.setLevel(logging.DEBUG)
    # create debug file handler and set level to debug
    # handler = logging.StreamHandler()
    # handler.setLevel(logging.INFO)
    #formatter = logging.Formatter("%(levelname)s - %(message)s")
    # handler.setFormatter(formatter)
    # logger.addHandler(handler)
    logging.info("!!!Problem:" + text)