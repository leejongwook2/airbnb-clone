from django.urls import path
from rooms import views as room_views

app_name="core"

# 요청하는것 , 요청에 반응하는 것 (이것들은 함수에만 반응함... 그래서 as_view() 가 필요한거야)
urlpatterns = [
    path("", room_views.HomeView.as_view(), name="home")
]




