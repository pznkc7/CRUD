from django.urls import path
from . views import *

urlpatterns = [
    path('', home, name='home'),
    path('form/', form, name='form'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]