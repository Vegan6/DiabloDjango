from django.shortcuts import render
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from DiabloDjango.AppData import models
from DiabloDjango.AppCode import DiabloAPI

def GetLeaderboard(data_point, season):
    #http://us.api.battle.net/oauth/token
    #https://us.battle.net/forums/en/bnet/topic/18724765570?page=1
    #https://us.battle.net/forums/en/bnet/topic/20749867301
    #token = models.DimensionConfig.objects.get(configname='AuthToken')
    
    """ Check if there is a token in the database """
    #if not token:
    token = DiabloAPI.AuthToken()
    
    
    
    boards = DiabloAPI.GetLeaderboards(token, data_point, season)
    
    return boards      
    
@csrf_exempt
def leaderboard(request):
    """Renders the leaderboard page."""
    assert isinstance(request, HttpRequest)    
    initial={'battletag': request.session.get('battletag', None)}
    try:
        HeroPortrait = request.session['heroportrait']
    except:
        HeroPortrait = ''
    
    data_point = request.POST.get("ddlLeaderboard", "rift-dh")
    season = request.POST.get("ddlSeason", "17");
    
    Leaderboards = GetLeaderboard(data_point, season)
    
    context = {
            'title': 'Leaderboards',
            'year': datetime.now().year,
            'UserName': '<li class="menuItem">' + str(initial['battletag']).replace('-', '#') + '</li>',
            'CharacterMenu': HeroPortrait,
            'Rows' : Leaderboards,
            'Selected' : data_point,
            "Season" : season
        }
    return render(
        request,
        'leaderboard.html',
        context
    )