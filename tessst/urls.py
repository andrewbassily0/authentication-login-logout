
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.tessst , name='tessst' ,  ),
    path('login', views.login_user , name='login' ),
    path('logout', views.logout_user , name='logout' ),
]