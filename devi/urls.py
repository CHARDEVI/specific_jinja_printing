from devi.views import *
from django.urls import path
app_name='dhoni'
urlpatterns=[
    path('csk/',csk,name='csk'),
]