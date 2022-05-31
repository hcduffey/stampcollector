from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .models import Stamp

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

class Stamp_List(TemplateView):
    template_name = 'stamp_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stamps"] = Stamp.objects.all()

        return context

class StampCreate(CreateView):
    model = Stamp
    fields = ["name", "image", "country", "condition", "centering", "format", "year"]
    template_name = "stamp_create.html"
    success_url = "/stamps/"