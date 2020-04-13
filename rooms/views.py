from math import ceil
from django.shortcuts import redirect, render
from datetime import datetime
from django.core.paginator import EmptyPage, Paginator
from . import models

def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10)
    try:
        rooms = paginator.page(int(page))
        return render(request, "rooms/home.html", context={"page": rooms})
    except EmptyPage:
        # rooms = paginator.page(1)
        # 니콜라스는 redirect를 더 선호한다고 한다.. 마법같지 않아서...
        return redirect("/")
