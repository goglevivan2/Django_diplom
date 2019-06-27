from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('showSignUp/', views.showSignUp),
    path('showSignIn/', views.showSignIn),
    path('SignIn/', views.SignIn),
]
