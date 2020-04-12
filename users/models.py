from django.contrib.auth.models import AbstractUser
from django.db import models

# 여기에 대부분은... models.Model 을 넣는다...
# mdoels 는 이건데??? 위에 상속된 models 저거랑 동치함...
# admin page 에서 본것들이 많아... AbstractUsera에...
class User(AbstractUser):

    bio = models.TextField(default="")


