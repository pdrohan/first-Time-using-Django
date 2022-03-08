from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from .models import Projects
from django.shortcuts import get_object_or_404

# Create your views here.
class ProjectListView(ListView):
    template_name = 'projects/projects-home.html'
    queryset = Projects.objects.all()