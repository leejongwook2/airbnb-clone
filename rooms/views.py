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
    #  view 를 list 하고 form 을 제출하고... 그러면 class based로는 힘들어...
    # 위의 model 데이터 외에 추가적으로 데이터를 더 보내고 싶다면 ... get_context_data 를 사용한다.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = datetime.now()
        context["now"] = now
        return context
