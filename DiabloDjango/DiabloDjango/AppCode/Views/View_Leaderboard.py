from django.shortcuts import render
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from DiabloDjango.AppData import models
from DiabloDjango.AppCode import DiabloAPI

def GetLeaderboard(data_point):
    #http://us.api.battle.net/oauth/token
    #https://us.battle.net/forums/en/bnet/topic/18724765570?page=1
    #https://us.battle.net/forums/en/bnet/topic/20749867301
    #token = models.DimensionConfig.objects.get(configname='AuthToken')
    
    """ Check if there is a token in the database """
    #if not token:
    token = DiabloAPI.AuthToken()
    
    
    
    boards = DiabloAPI.GetLeaderboards(token, data_point)
    
    return boards      
    
@csrf_exempt
def leaderboard(request):
    """Renders the leaderboard page."""
    assert isinstance(request, HttpRequest)    
    
    data_point = request.POST.get("leaderboard", "rift-necromancer")
        
    Leaderboards = GetLeaderboard(data_point)
    
    context = {
            'title': 'Leaderboards',
            'year': datetime.now().year,
            'Rows' : Leaderboards,
            'Selected' : data_point
        }
    return render(
        request,
        'leaderboard.html',
        context
    )