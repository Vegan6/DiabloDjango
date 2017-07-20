from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    context_instance = {
        'title': 'Contact',
        'message': 'Your contact page.',
        'year': datetime.now().year,
    }
    return render(
        request,
        'contact.html',
        context_instance
    )