from django.urls import path
from .views import *
from django.contrib import admin

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home, name='home'),
    path(r'^login/$', auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),
    path(r'^logout/$', auth_views.LogoutView.as_view(template_name="registration/logged_out.html"), name='logout'),

    path('password/change/', auth_views.PasswordChangeView.as_view(template_name="registration/password_change_form.html"), name='password_change'),
    path('password/change/done/', auth_views.PasswordChangeDoneView.as_view(template_name="registration/password_change_done.html"), name='password_change_done'),
    path('password/reset/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"), name='password_reset'),
    path('password/reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), name='password_reset_done'),

    path('tours/', TourListView.as_view(), name='tours'),
    path('agents/', AgentListView.as_view(), name='agents'),
    path('tours/<int:pk>/', TourDetailView.as_view(), name='tour_detail'),

    path('tours_by_agent/', ToursByAgentView.as_view(), name='tours_by_agent'),
]
