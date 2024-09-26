
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('login/', views.login_user, name = 'login'),
    path('logout/', views.logout_user, name = 'logout'),
    path('signin/', views.signin_user, name = 'signin'),
    path('collection/', views.collection, name = 'collection'),
    path('asset/<int:pk>', views.asset, name = 'asset'),
]
