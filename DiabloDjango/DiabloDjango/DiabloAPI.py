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

# Load Hero Profile
# Returns JSON Object
def HeroProfile(Host, BattleTag, HeroId):
    url = "%s/d3/profile/%s/hero/%s?%s&%s" % (Host, BattleTag, HeroId, EN_LOCALE, API_KEY)
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        raise Exception('Error:\n' + response.text)