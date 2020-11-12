from django.urls import path

from pyprojat.turmas import views

app_name = 'turmas'
urlpatterns = [
    path('', views.indice, name='indice'),
]
