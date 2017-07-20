from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    context_instance = {
        'title': 'About',
        'message': 'Your application description page.',
        'year': datetime.now().year,
    }
    return render(
        request,
        'about.html',
        context_instance
    )