from cherry.views import *
from django.urls import path
app_name='virat'
urlpatterns=[
    path('rcb/',rcb,name='rcb'),
]