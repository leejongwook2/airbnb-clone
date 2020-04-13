from django.contrib import admin
from . import models

@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ ItemAdmin Definition """

    list_display=("name","used_by",)

    # 이렇게 할 수 있는 이유는 roomType, amenity, facility, houserule 모두 rooms 라고 걸어놔서 가능한거야...
    #  그런데 문제는 !! 어떻게 접근을 할수 있었는가를 아는것이 핵심이지 .. 있다가 공부해야함 .이 부분
    def used_by(self, obj):
        return obj.rooms.count()

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

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

    pass