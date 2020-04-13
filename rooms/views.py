from math import ceil
from django.shortcuts import render
from datetime import datetime
from django.core.paginator import Paginator
from . import models

def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10)
    rooms = paginator.page(int(page))
    return render(request, "rooms/home.html", context={"page": rooms})
