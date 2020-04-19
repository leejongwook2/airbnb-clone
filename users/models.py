from django.contrib.auth.models import AbstractUser
from django.db import models

# 여기에 대부분은... models.Model 을 넣는다...
# mdoels 는 이건데??? 위에 상속된 models 저거랑 동치함...
# admin page 에서 본것들이 많아... AbstractUsera에...
class User(AbstractUser):

    """ User Model Definition """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KROEAN = "kr"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KROEAN, "Korean"),
    )

    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGIN_KAKAO ="kakao"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_GITHUB, "Github"),
        (LOGIN_KAKAO, "Kakao"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW"),
    )

    # blank =True 로 주어야지... 유저 만들 때 안적어줘도 된다...실제로 회원가입시에... 기입이 필요하지 않아....
    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, default=GENDER_MALE, max_length=10, blank=True)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True, default=LANGUAGE_KROEAN)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True, default=CURRENCY_KRW)
    superhost = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)
    login_method = models.CharField(choices=LOGIN_CHOICES, max_length=50, default=LOGIN_EMAIL)

    def __str__(self):
        return self.username


