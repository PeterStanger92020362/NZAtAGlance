from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('signin/', signin, name='signin'),
    path('tours/', TourListView.as_view(), name='tours'),
    path('agents/', AgentListView.as_view(), name='agents'),
    path('tours/<int:pk>/', TourDetailView.as_view(), name='tour_detail')
]
