from django.urls import path

from.views import IndexPage, LoginPage, RegisterPage


urlpatterns = [
    path('', IndexPage.as_view(), name='home'),
    path('login', LoginPage.as_view(), name='login'),
    path('register', RegisterPage.as_view(), name='register'),
]