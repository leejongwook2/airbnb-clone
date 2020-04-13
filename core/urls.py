from django.urls import path
from rooms import views as room_views

app_name="core"

# 요청하는것 , 요청에 반응하는 것
urlpatterns = [
    path("", room_views.all_rooms, name="home")
]




