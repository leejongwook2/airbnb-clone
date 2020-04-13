from django.contrib import admin
from django.utils.html import mark_safe
from . import models

@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ ItemAdmin Definition """

    list_display=("name","used_by",)

    # 이렇게 할 수 있는 이유는 roomType, amenity, facility, houserule 모두 rooms 라고 걸어놔서 가능한거야...
    #  그런데 문제는 !! 어떻게 접근을 할수 있었는가를 아는것이 핵심이지 .. 있다가 공부해야함 .이 부분
    def used_by(self, obj):
        return obj.rooms.count()

class PhotoInline(admin.TabularInline):

    model = models.Photo

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    inlines = (PhotoInline,)

    fieldsets = (
        ("Basic Info", {
            "fields": (
                "name", "description", "country", "address", "price"
            ),
        }),
        ("Times", {
            "fields": (
                "check_in", "check_out", "instant_book"
            ),
        }),
        ("Spaces", {
            "fields": (
                "guests",
                "beds",
                "bedrooms",
                "baths"
            ),
        }),
        ("More About the Sapce", {
            "classes": ("collapse",),
            "fields": (
                "amenities",
                "facilities",
                "house_rules",
            ),
        }),
        ("Last Details", {
            "fields": ("host",)
        }),
    )


    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    # ordering = ("name", "price", "bedrooms")

    list_filter = ("instant_book", "host__superhost", "city", "country", "room_type", "amenities", "facilities", "house_rules")

    # host 를 검색 할 수 있게 해준다. 유저가 많을 떄 검색 할 수 있어서 좋다.
    raw_id_fields = ("host",)

    search_fields = ["city", "^host__username"]

    # many tomany 만 가능한거야 이거는...
    filter_horizontal = ("amenities", "facilities", "house_rules")

    # self 는 class 고 self 는 현재 row를 가르킴
    def count_amenities(self, obj):
        print(obj.amenities.all())
        return obj.amenities.count()
    count_amenities.short_description = "amenities count"

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        # obj.file 프린트 해보면 ... url 이라는 변수가 있구나.. 있어!!
        return mark_safe(f"<img width='80px' src='{obj.file.url}'/>")
    get_thumbnail.short_description = "Thumbnail"