from django.urls import path
from comunidade import views

app_name = 'comunidade'

urlpatterns = [
    path('comunidade/', views.comunidade, name='comunidade')
]