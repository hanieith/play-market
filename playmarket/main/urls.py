from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('app_info/', app_info, name='app_info')
]
