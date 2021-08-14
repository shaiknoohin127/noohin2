from django.urls import path
from app.views import *
app_name='app'
urlpatterns=[
    path('specific1/',specific1,name='specific1'),
]