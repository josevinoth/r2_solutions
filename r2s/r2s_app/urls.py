from django.urls import path
from . import views
from django.contrib.auth import views as auth_views #import this
urlpatterns = [
    path('home/', views.home_view, name='home'),  # open home page
    path('first_page/', views.first_page_view, name='first_page'),  # open home page

]