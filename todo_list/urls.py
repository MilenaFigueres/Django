from django.conf.urls import url, include
from django.contrib import admin
'''from django.conf.urls import patterns, include, url  
from ads.views import PostAdPage
#from . import views'''

urlpatterns = [
    url('', admin.site.urls),
    #url(r'^postad/', PostAdPage.as_view()),
    #url('add/', views.PersonalListCreateView, name='PersonalListCreateView'),

    #DESCOMENTAR
    #url(r'^admin/', admin.site.urls),
    #url(r'', include('lists.urls')),
]
