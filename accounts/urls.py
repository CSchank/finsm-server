from django.urls import path
from . import views
from django.conf.urls import url, include
from django.contrib.auth import views as authviews

urlpatterns = [
    path('loginstate/', views.loginstate, name='loginstate'),
    url(r'^login/$', authviews.LoginView.as_view(), name='login'),
    url(r'^logout/$', authviews.LogoutView.as_view(), name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),  # <- Here
    url(r'^$', views.home, name='home'),
]