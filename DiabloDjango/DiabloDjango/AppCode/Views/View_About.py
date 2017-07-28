from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    initial={'battletag': request.session.get('battletag', None)}
    try:
        HeroPortrait = request.session['heroportrait']
    except:
        HeroPortrait = ''
        
    context_instance = {
        'title': 'About',
        'message': 'Your application description page.',
        'year': datetime.now().year,
        'UserName': '<li class="menuItem">' + str(initial['battletag']).replace('-', '#') + '</li>',
        'CharacterMenu': HeroPortrait,
    }
    return render(
        request,
        'about.html',
        context_instance
    )