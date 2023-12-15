from django.urls import path
from arena import views

app_name = 'arena'

urlpatterns = [
    path('arena/', views.arena, name='arena')
]