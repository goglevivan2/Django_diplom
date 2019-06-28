from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('showSignUp/', views.showSignUp),
    path('showSignIn/', views.showSignIn),
    path('SignIn/', views.SignIn),
    path('SignUp/', views.SignUp),
    path('shop/', views.shop),
]
