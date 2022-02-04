from django.urls import URLPattern, path
from main import views

urlpatterns = [
    path('',views.index,name='index')

]