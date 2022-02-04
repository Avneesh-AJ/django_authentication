from urllib import request
from django.urls import URLPattern, path    

from auth import views

urlpatterns=[
    path('login/',views.login)
]