"""
Definition of error views.
"""

import sys;

from django.shortcuts import render
#from django.http import HttpRequest
#from django.template import RequestContext
from .helper import *
#import traceback
#import sys


def handler400(request):
    response = render_to_response('error.html', {}, context_instance=RequestContext(request))
    response.status_code = 400
    return response


def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    #response = render_to_response('500.html', {}, context_instance=RequestContext(request))
    request.status_code = 500
    context_instance = {
        "error": sys.exc_info()
    }
    return render(
        request,
        '500.html',
        context_instance
    )