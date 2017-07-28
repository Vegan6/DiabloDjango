from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    initial={'battletag': request.session.get('battletag', None)}
    try:
        HeroPortrait = request.session['heroportrait']
    except:
        HeroPortrait = ''
    context_instance = {
        'title': 'Contact',
        'message': 'Your contact page.',
        'year': datetime.now().year,
        'UserName': '<li class="menuItem">' + str(initial['battletag']).replace('-', '#') + '</li>',
        'CharacterMenu': HeroPortrait,
    }
    return render(
        request,
        'contact.html',
        context_instance
    )