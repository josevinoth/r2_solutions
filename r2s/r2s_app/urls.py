from django.urls import path
from . import views
from django.contrib.auth import views as auth_views #import this
urlpatterns = [
    path('home/', views.home_view, name='home'),  # open home page

]