"""
Definition of urls for DiabloDjango.
"""

#from datetime import datetime
#from django.conf.urls import patterns
from django.conf.urls import url
#import DiabloDjango.AppCode.views
import DiabloDjango.AppCode.Views.View_Career
import DiabloDjango.AppCode.Views.View_Home
import DiabloDjango.AppCode.Views.View_Hero
import DiabloDjango.AppCode.Views.View_Toolbox
import DiabloDjango.AppCode.Views.View_Contact
import DiabloDjango.AppCode.Views.View_About
import DiabloDjango.AppCode.Views.View_Leaderboard

# Uncomment the next lines to enable the admin:
#from django.conf.urls import include

handler500 = 'DiabloDjango.AppCode.views.handler500'

urlpatterns = [
    url(r'^$', DiabloDjango.AppCode.Views.View_Home.home),
    url(r'^hero', DiabloDjango.AppCode.Views.View_Hero.hero),
    url(r'^career', DiabloDjango.AppCode.Views.View_Career.career),
    url(r'^leaderboard', DiabloDjango.AppCode.Views.View_Leaderboard.leaderboard),
    url(r'^toolbox', DiabloDjango.AppCode.Views.View_Toolbox.toolbox),
    url(r'^contact', DiabloDjango.AppCode.Views.View_Contact.contact),
    url(r'^about', DiabloDjango.AppCode.Views.View_About.about),

   #url(r'^login/$',
   #     'django.contrib.auth.views.login',
   #     {
   #         'template_name': 'app/login.html',
   #         'authentication_form': BootstrapAuthenticationForm,
   #         'extra_context':
   #         {
   #             'title': 'Log in',
   #             'year': datetime.now().year,
   #         }
   #     },
   #     name='login'),
   # url(r'^logout$',
   #     'django.contrib.auth.views.logout',
   #     {
   #         'next_page': '/',
   #     },
   #     name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    ]
