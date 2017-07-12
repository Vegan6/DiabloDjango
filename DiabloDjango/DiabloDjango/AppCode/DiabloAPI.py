import requests
import json
import logging
import os.path
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