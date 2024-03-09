from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('registration/', UserDetails.as_view(), name='register'),
    path('login/',LoginUser.as_view(), name='login'),
]