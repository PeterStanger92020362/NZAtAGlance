from django.http.response import HttpResponse, HttpResponseRedirect
from NZAtAGlance.forms import ChangeAgent
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Tour, Agent



"""
The classes defined below are function based view (FBV).
"""
@login_required
def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'registration/login.html')

@login_required
def logout(request):
    return render(request, 'registration/logged_out.html')


"""
The classes defined below are class based view (CBV).

if you use ListView, you have to define the corresponding model
(decalred in models.py under home). As ListView is used to do the
interaction with Database.
"""

class TourListView(LoginRequiredMixin, ListView):
    queryset = Tour.objects.all().order_by('tour_name')

    # setup template file
    template_name = 'tours.html'

    # setup “friendly” template context
    # if not set up, 'tour_list' used as default
    # setting 'context_object_name' is always a good idea
    context_object_name = 'tours'

    # setup how many data to display per page
    paginate_by = 10


class AgentListView(LoginRequiredMixin, ListView):
    queryset = Agent.objects.all().order_by('agent_username')

    # setup template file
    template_name = 'agents.html'

    context_object_name = 'agents'

    # setup how many data to display per page
    paginate_by = 10


class TourDetailView(LoginRequiredMixin, DetailView):
    queryset = Tour.objects.all().order_by('tour_name')

    template_name = 'tour_detail.html'

    context_object_name = 'tour'


class ToursByAgentView(LoginRequiredMixin, ListView):

    queryset = Tour.objects.filter(agent_id=1)
  
   
    template_name = 'tours_by_agent.html'

    context_object_name = 'tours'

    paginate_by = 10


class AgentDetailView(LoginRequiredMixin, DetailView):
    queryset = Agent.objects.all().order_by('agent_username')

    template_name = 'agent_detail.html'

    context_object_name = 'agent'
