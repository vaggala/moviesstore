"""
import path function
then import views file
implement index function inside views file
define urlpatterns
- root url is empty, 
- then views.indexc == http req, 
- then home.index = name of url pattern
"""
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home.index'),
    path('about', views.about, name='home.about')
]
