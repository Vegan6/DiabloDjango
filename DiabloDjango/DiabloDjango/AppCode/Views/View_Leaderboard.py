from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
from DiabloDjango.AppData import models
from DiabloDjango.AppCode import DiabloAPI

def GetLeaderboard():
    #http://us.api.battle.net/oauth/token
    #https://us.battle.net/forums/en/bnet/topic/18724765570?page=1
    #https://us.battle.net/forums/en/bnet/topic/20749867301
    #token = models.DimensionConfig.objects.get(configname='AuthToken')
    
    """ Check if there is a token in the database """
    #if not token:
    token = DiabloAPI.AuthToken()
    
    boards = DiabloAPI.GetLeaderboards(token)
    
    return boards
        
    
    

def leaderboard(request):
    """Renders the leaderboard page."""
    assert isinstance(request, HttpRequest)
    Leaderboards = GetLeaderboard()
    
    context = {
            'title': 'Leaderboards',
            'year': datetime.now().year,
            'Rows' : Leaderboards
        }
    return render(
        request,
        'leaderboard.html',
        context
    )