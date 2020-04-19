import os
import requests
from django.views import View
from django.views.generic import FormView
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.core.files.base import ContentFile
from . import models
from . import forms

class LoginView(FormView):

    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))

    """ def login_view(request):

    if request.method == "GET": """

class SignUpView(FormView):

    template_name = "users/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("core:home")
    initial = {
        "first_name": "lee",
        "last_name": "fklsks",
        "email": "net1500@naver.com"
    }

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

def github_login(reuqest):
    client_id = os.environ.get("GITHUB_USERID")
    redirect_uri = "http://127.0.0.1:8000/users/login/github/callback"
    return redirect(f"https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&scope=read:user")

class GithubException(Exception):
    pass


def github_callback(request):
    try:
        client_id = os.environ.get("GITHUB_USERID")
        client_secret = os.environ.get("GITHUB_SECRET")
        code = request.GET.get("code", None)
        if code is not None:
            token_request = requests.post(
                f"https://github.com/login/oauth/access_token?client_id={client_id}&client_secret={client_secret}&code={code}",
                headers={"Accept": "application/json"},
            )
            token_json = token_request.json()
            error = token_json.get("error", None)
            if error is not None:
                raise GithubException()
            else:
                access_token = token_json.get("access_token")
                profile_request = requests.get(
                    "https://api.github.com/user",
                    headers={
                        "Authorization": f"token {access_token}",
                        "Accept": "application/json",
                    },
                )
                profile_json = profile_request.json()
                username = profile_json.get("login", None)
                if username is not None:
                    name = profile_json.get("login")
                    email = f"{name}@korea.com"
                    bio = profile_json.get("id")
                    try:
                        user = models.User.objects.get(email=email)
                        if user.login_method != models.User.LOGIN_GITHUB:
                            raise GithubException()
                    except models.User.DoesNotExist:
                        user = models.User.objects.create(
                            email=email,
                            first_name=name,
                            username=email,
                            bio=bio,
                            login_method=models.User.LOGIN_GITHUB,
                            email_verified = True
                        )
                        user.set_unusable_password()
                        user.save()
                    login(request, user)
                    return redirect(reverse("core:home"))
                else:
                    raise GithubException()
        else:
            raise GithubException()
    except GithubException:
        # send error message
        return redirect(reverse("users:login"))

def kakao_login(request):
    app_key = os.environ.get("KAKAO_KEY")
    redirect_uri = "http://127.0.0.1:8000/users/login/kakao/callback"
    return redirect(f"https://kauth.kakao.com/oauth/authorize?client_id={app_key}&redirect_uri={redirect_uri}&response_type=code")

class KakaoException(Exception):
    pass

def kakao_callback(request):
    try:
        code = request.GET.get("code")
        app_key = os.environ.get("KAKAO_KEY")
        redirect_uri = "http://127.0.0.1:8000/users/login/kakao/callback"
        token_request = requests.get(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={app_key}&redirect_uri={redirect_uri}&code={code}"
        )
        token_json = token_request.json()
        error = token_json.get("error", None)
        if error is not None:
            raise KakaoException()
        access_token = token_json.get("access_token")
        profile_request = requests.get("https://kapi.kakao.com/v2/user/me",
        headers={"Authorization":f"Bearer {access_token}"},
        )
        profile_json = profile_request.json()
        account = profile_json.get("kakao_account", None)
        if account is not None:
            email = account.get("email", None)
            if email is None:
                raise KakaoException()
            profile = account.get("profile")
            nickname = profile.get("nickname")
            profile_image_url = profile.get("profile_image_url")
            try:
                user = models.User.objects.get(email=email)
                if user.login_method != models.User.LOGIN_KAKAO:
                    raise KakaoException()
            except models.User.DoesNotExist:
                user = models.User.objects.create(
                    email=email,
                    username = email,
                    first_name = nickname,
                    login_method = models.User.LOGIN_KAKAO,
                    email_verified = True
                )
                user.set_unusable_password()
                user.save()
                if profile_image_url is not None:
                    photo_reuqest = requests.get(profile_image_url)
                    user.avatar.save(
                        f"{nickname}-avatar", ContentFile(photo_reuqest.content)
                    )
                    print(ContentFile(photo_reuqest.content))
                    print(ContentFile(photo_reuqest.content))
                    print(ContentFile(photo_reuqest.content))
                    print(ContentFile(photo_reuqest.content))
                    print(ContentFile(photo_reuqest.content))
            login(request, user)
            return redirect(reverse("core:home"))
        else :
            raise KakaoException()

    except KakaoException:
        return redirect(reverse("users:login"))





