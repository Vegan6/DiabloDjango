from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
from django.http import HttpResponseRedirect
from DiabloDjango.AppCode.Forms import HomeForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    initial={'battletag': request.session.get('battletag', None)}
    form = HomeForm.HomeForm(request.POST or None, initial=initial)
    try:
        HeroPortrait = request.session['heroportrait']
    except:
        HeroPortrait = ''
    if request.method == 'POST':
        if form.is_valid():
            request.session['battletag'] = form.cleaned_data['battletag']
            return HttpResponseRedirect('/career')
        
    context = {
            'title': 'Diablo 3',
            'year': datetime.now().year,
            'form': form,
            'UserName': '<li class="menuItem">' + str(initial['battletag']).replace('-', '#') + '</li>',
            'CharacterMenu': HeroPortrait,
        }
    return render(
        request,
        'index.html',
        context
    )