from django.urls import path
from . import views
from django.contrib.auth import views as auth_views #import this
urlpatterns = [
    path('home/', views.home_view, name='home'),  # open home page
    path('first_page/', views.first_page_view, name='first_page'),  # open first page
    path('second_page/', views.second_page_view, name='second_page'),  # open second page
    path('third_page/', views.third_page_view, name='third_page'),  # open third page
    path('fourth_page/', views.fourth_page_view, name='fourth_page'),  # open fourth page


]