from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Tour, Agent

"""
The classes defined below are function based view (FBV).
"""
def home(request):
    return render(request, 'index.html')


def signin(request):
    return render(request, 'signin.html')

"""
The classes defined below are class based view (CBV).

if you use ListView, you have to define the corresponding model
(decalred in models.py under home). As ListView is used to do the
interaction with Database.
"""

class TourListView(ListView):
    queryset = Tour.objects.all().order_by('tour_name')

    # setup template file
    template_name = 'tours.html'

    # setup “friendly” template context
    # if not set up, 'tour_list' used as default
    # setting 'context_object_name' is always a good idea
    context_object_name = 'tours'

    # setup how many data to display per page
    paginate_by = 10


class AgentListView(ListView):
    queryset = Agent.objects.all().order_by('agent_username')

    # setup template file
    template_name = 'agents.html'

    context_object_name = 'agents'

    # setup how many data to display per page
    paginate_by = 10


class TourDetailView(DetailView):
    queryset = Tour.objects.all().order_by('tour_name')

    template_name = 'tour_detail.html'

    context_object_name = 'tour'
