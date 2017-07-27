from django import forms

class HomeForm(forms.Form):
    battletag = forms.CharField(label='BattleTag', max_length=100)
    battletag.widget.attrs.update({'class' : 'homeform'})