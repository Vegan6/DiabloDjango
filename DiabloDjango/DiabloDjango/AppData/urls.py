"""
Definition of urls for DiabloDjango.
"""

from datetime import datetime
from django.conf.urls import patterns, url

# Uncomment the next lines to enable the admin:
#from django.conf.urls import include

urlpatterns = patterns('',
    url(r'^$', 'DiabloDjango.AppCode.views.home', name='home'),
    url(r'^hero', 'DiabloDjango.AppCode.views.hero', name='hero'),
    url(r'^career', 'DiabloDjango.AppCode.views.career', name='career'),

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

)
