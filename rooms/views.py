from django.shortcuts import render
from datetime import datetime
from . import models

def all_rooms(request):
    page = request.GET.get("page")
    page = int(page or 1)
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_rooms = models.Room.objects.all()[offset:limit]
    return render(request, "rooms/home.html", context={
        "rooms": all_rooms
    })
