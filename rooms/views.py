from django.shortcuts import redirect, render
from django_countries import countries
from django.http import Http404
from datetime import datetime
from django.views.generic import ListView, DetailView
from django.core.paginator import EmptyPage, Paginator
from . import models
from django.urls import reverse

class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    ordering = "created"
    context_object_name = "rooms"
    # page_kwarg : page keyword argument
    #  view 를 list 하고 form 을 제출하고... 그러면 class based로는 힘들어...
    # 위의 model 데이터 외에 추가적으로 데이터를 더 보내고 싶다면 ... get_context_data 를 사용한다.

    """
    def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", context={"room" : room})
    except models.Room.DoesNotExist:
        # return redirect(reverse("core:home"))
        raise Http404() """


    """
        def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = datetime.now()
        context["now"] = now
        return context
    """


class RoomDetail(DetailView):

    """ RoomDetail Definition """

    model = models.Room
    # pk_url_kwarg = "potato" pk 이름을 변경 할 수 있다.. ㅇㅇ

def search(request):
    city = request.GET.get("city", "AnyWhere")
    city = str.capitalize(city)
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", 0))

    room_types = models.RoomType.objects.all()

    form = {
        "city": city,
        "s_country": country,
        "s_room_type": room_type
    }

    choices = {
        "countries": countries,
        "room_types": room_types
    }

    return render(request, "rooms/search.html",
    context={
        **form,**choices
    }
)
