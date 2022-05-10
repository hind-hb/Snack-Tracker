from pyexpat import model
from re import template
from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Snack

# Create your views here.
class SnackView(ListView):
    template_name = "Snack_list.html"
    model = Snack
    context_object_name = "Snack_list"

class SnackDescrptionView(DetailView):
    template_name = "snack_detail.html"
    model = Snack


