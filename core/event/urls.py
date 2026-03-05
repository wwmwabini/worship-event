from django.urls import path
from event import views as event_views

urlpatterns = [
    path('', event_views.event_home, name='event_home')
]