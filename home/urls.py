from django.urls import path
from .views import *
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path(r'^login/$', auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),
    path(r'^logout/$', auth_views.LogoutView.as_view(template_name="registration/logged_out.html"), name='logout'),
    path('tours/', TourListView.as_view(), name='tours'),
    path('agents/', AgentListView.as_view(), name='agents'),
    path('tours/<int:pk>/', TourDetailView.as_view(), name='tour_detail')
]
