from math import ceil
from django.shortcuts import redirect, render
from datetime import datetime
from django.views.generic import ListView
from django.core.paginator import EmptyPage, Paginator
from . import models

class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    ordering = "created"
    context_object_name = "rooms"
    # page_kwarg : page keyword argument
