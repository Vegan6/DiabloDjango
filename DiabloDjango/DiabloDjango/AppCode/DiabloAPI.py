import requests
import json
from .DiabloObjects import DiabloAPIConfig
from .DiabloObjects import Hero
from .DiabloObjects import Career

# Load Career
# Returns Career Class


def GetCareer(Host, BattleTag):
    DiabloAPIConfig.CURRENTSERVER = Host
    DiabloAPIConfig.BATTLETAG = BattleTag
    url = "%s/d3/profile/%s/?%s&%s" % (DiabloAPIConfig.CURRENTSERVER, DiabloAPIConfig.BATTLETAG, DiabloAPIConfig.EN_LOCALE, DiabloAPIConfig.API_KEY)
    response = requests.get(url)
    response
    if response.status_code == 200:
        return Career.Career(json.loads(response.text))
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