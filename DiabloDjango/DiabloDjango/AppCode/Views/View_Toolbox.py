from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
from DiabloDjango.AppCode import DiabloAPI
from DiabloDjango.AppCode.DiabloObjects import DiabloAPIConfig
from DiabloDjango.AppCode.DiabloObjects import Career


def toolbox(request):
    """Renders the Toolbox page."""
    assert isinstance(request, HttpRequest)
    BattleTag = request.GET.get('battletagcareer')
    if not BattleTag:
        CareerDetails = Career.Career(request.session['CareerProfile'])
    else:
        CareerDetails = DiabloAPI.GetCareer(DiabloAPIConfig.US_SERVER, BattleTag)
        request.session['CareerProfile'] = CareerDetails
    HeroPortrait = ""
    heroes = CareerDetails.Heroes()
    for hero in heroes:
        HeroPortrait += hero.Portrait
    context_instance = {
        'Title': 'Diablo 3',
        'Year': datetime.now().year,
        'UserName': CareerDetails.BattleTagDisplay,
        'CharacterMenu': HeroPortrait,
    }
    return render(
        request,
        'toolbox.html',
        context_instance
    )