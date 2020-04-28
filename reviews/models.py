from django.db import models
from core import models as core_models

class Review(core_models.TimeStampedModel):

    """ Review Model Definition """

    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey("users.User", related_name="reviews", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", related_name="reviews", on_delete=models.CASCADE)

    # 나라 접근이 가능함... 헐 ... FOREIGNKEY 의 ...
    def __str__(self):
        # return self.room.country
        # return self.room.host.email
        return f"{self.review} -------- {self.room}"

    #  전체에서 사요되니깐... admin 에 함수를 만들지 않았다.
    #  admin 만을 위한 함수를 생성할 것인지.. 공통적으로 포함된 함수를 만들것인지... 고민해봐요
    def rating_average(self):
        avg = (
            self.accuracy +
            self.communication +
            self.cleanliness +
            self.location +
            self.check_in +
            self.value
        )/6
        avg = round(avg, 2)
        return avg
    rating_average.short_description = "AVG."



