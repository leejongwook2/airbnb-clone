from django.contrib import admin
from . import models

@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ ItemAdmin Definition """

    pass

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
    )

    # ordering = ("name", "price", "bedrooms")

    list_filter = ("instant_book", "host__superhost", "city", "country", "room_type", "amenities", "facilities", "house_rules")

    search_fields = ["city", "^host__username"]

    # many tomany 만 가능한거야 이거는...
    filter_horizontal = ("amenities", "facilities", "house_rules")

    # self 는 class 고 self 는 현재 row를 가르킴
    def count_amenities(self, obj):
        print(obj.amenities.all())
    count_amenities.short_description = "amenities count"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    pass