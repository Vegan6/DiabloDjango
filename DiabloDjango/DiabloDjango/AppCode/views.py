"""
Definition of error views.
"""

import sys
import traceback

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

    type, value, tb = sys.exc_info()

    error = traceback.format_exception(type, value, tb)
    #error = type.__name__ + ":" + value
    #error += '\n'.join(traceback.format_tb(tb))
    #error += '\n' + sys.exc_info()

    context_instance = {
        "error": error
    }
    return render(
        request,
        '500.html',
        context_instance
    )