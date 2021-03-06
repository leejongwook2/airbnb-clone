from django.db import models
from core import models as core_models

class List(core_models.TimeStampedModel):

    """ List Model Definition """

    name = models.CharField(max_length=80)
    user = models.ForeignKey("users.User", related_name="lists", on_delete=models.CASCADE)
    # list 가 방을 여러개 가질수 있다.. 그러면 그냥 manyto many 로 걸어주나 본데??
    rooms = models.ManyToManyField("rooms.Room", related_name="lists", blank=True)

    def __str__(self):
        return self.name

    def count_rooms(self):
        return self.rooms.count()
    count_rooms.short_description = "Number Of Rooms"
