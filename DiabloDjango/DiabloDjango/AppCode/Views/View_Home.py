from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    context = {
            'title': 'Diablo 3',
            'year': datetime.now().year,
        }
    return render(
        request,
        'index.html',
        context
    )