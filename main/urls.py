from django.urls import URLPattern, path
from main import views

urlpatterns = [
    path('',views.index,name='index'),
    path('secure/',views.sshh,name='sshh')

]