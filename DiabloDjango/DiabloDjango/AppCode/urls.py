"""
Definition of urls for DiabloDjango.
"""

#from datetime import datetime
#from django.conf.urls import patterns, url
from django.conf.urls import url
import DiabloDjango.AppCode.views

# Uncomment the next lines to enable the admin:
#from django.conf.urls import include

urlpatterns = [
    url(r'^$', DiabloDjango.AppCode.views.home),
    url(r'^hero', DiabloDjango.AppCode.views.hero),
    url(r'^career', DiabloDjango.AppCode.views.career),
    url(r'^toolbox', DiabloDjango.AppCode.views.toolbox),
    url(r'^contact', DiabloDjango.AppCode.views.contact),
    url(r'^about', DiabloDjango.AppCode.views.about),

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
