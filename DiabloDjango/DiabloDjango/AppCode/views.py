"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from DiabloDjango.AppCode.DiabloAPI import *



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    #query = request.GET.get('hello', '')
    return render(
        request,
        'index.html',
        context_instance=RequestContext(request,
        {
            'title': 'Diablo 3',
            'year': datetime.now().year,
            'HeroProfile': 'No Hero Found',
                #+ "\nHero Name: " + HeroProfile['name']
                #+ "\nParagon Level: " + str(HeroProfile['paragonLevel'])
                #+ "\nClass: " + HeroProfile['class'],
        })
    )


def hero(request):
    """Renders the hero page."""
    assert isinstance(request, HttpRequest)
    if (request.GET.get('GetHero')):
        BattleTag = request.GET.get('battletag')
        HeroID = int(request.GET.get('heroid'))
        HerosProfile = HeroProfile(US_SERVER, BattleTag, HeroID)
    else:
        HerosProfile = ''
    return render(
        request,
        'hero.html',
        context_instance=RequestContext(request,
        {
            'title': 'Diablo 3',
            'year': datetime.now().year,
            'HeroProfile':
                "\nHero Name: " + HerosProfile['name']
                + "\nParagon Level: " + str(HerosProfile['paragonLevel'])
                + "\nClass: " + HerosProfile['class'],
        })
    )


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'Pages/contact.html',
        context_instance=RequestContext(request,
        {
            'title': 'Contact',
            'message': 'Your contact page.',
            'year': datetime.now().year,
        })
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'Pages/about.html',
        context_instance=RequestContext(request,
        {
            'title': 'About',
            'message': 'Your application description page.',
            'year': datetime.now().year,
        })
    )
