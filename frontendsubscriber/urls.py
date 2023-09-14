from django.urls import path
from .views import GetSubscriber

urlpatterns = [
    path('subscriber/', GetSubscriber),
]