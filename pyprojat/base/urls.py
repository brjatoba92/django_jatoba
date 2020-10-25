from django.urls import path

from pyprojat.base.views import home

app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
]
