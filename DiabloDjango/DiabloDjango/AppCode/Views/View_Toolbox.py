from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime


def toolbox(request):
    """Renders the Toolbox page."""
    assert isinstance(request, HttpRequest)
    initial={'battletag': request.session.get('battletag', None)}
    try:
        HeroPortrait = request.session['heroportrait']
    except:
        HeroPortrait = ''
    context_instance = {
        'Title': 'Diablo 3',
        'Year': datetime.now().year,
        'UserName': '<li class="menuItem">' + str(initial['battletag']).replace('-', '#') + '</li>',
        'CharacterMenu': HeroPortrait,
    }
    return render(
        request,
        'toolbox.html',
        context_instance
    )