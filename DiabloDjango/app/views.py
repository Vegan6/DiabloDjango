"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from DiabloDjango import DiabloAPI


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    HeroProfile = DiabloAPI.HeroProfile(DiabloAPI.US_SERVER, 'Heretic-1984', '64346468')
    query = request.GET.get('hello', '')
    return render(
        request,
        'app/index.html',
        context_instance=RequestContext(request,
        {
            'title': 'Diablo 3',
            'year': datetime.now().year,
            'HeroProfile': str(query)
                + "Hero Name: " + HeroProfile['name']
                + " Paragon Level:" + str(HeroProfile['paragonLevel']),
        })
    )


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
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
        'app/about.html',
        context_instance=RequestContext(request,
        {
            'title': 'About',
            'message': 'Your application description page.',
            'year': datetime.now().year,
        })
    )
