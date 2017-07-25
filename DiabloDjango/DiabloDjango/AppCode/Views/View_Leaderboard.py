from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime


def leaderboard(request):
    """Renders the leaderboard page."""
    assert isinstance(request, HttpRequest)
    context = {
            'title': 'Leaderboards',
            'year': datetime.now().year,
        }
    return render(
        request,
        'leaderboard.html',
        context
    )