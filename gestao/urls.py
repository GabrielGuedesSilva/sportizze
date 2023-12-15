from django.urls import path
from gestao import views

app_name = 'gestao'

urlpatterns = [
    path('gestao/', views.gestao, name='gestao')
]