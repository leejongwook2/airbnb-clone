import os
import requests
from django.views import View
from django.views.generic import FormView
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
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
            result = requests.post(
                    f"https://github.com/login/oauth/access_token?client_id={client_id}&client_secret={client_secret}&code={code}",
                    headers={"Accept": "application/json"},
            )
            result_json = result.json()
            error = result_json.get("error", None)
            if error is not None:
                raise GithubException()
            else :
                # 여기서 토큰을 받아오는구만....
                access_token = result_json.get("access_token")
                api_request = requests.get(
                    "https://api.github.com/user",
                    headers={
                        "Authorization": f"token {access_token}",
                        "Accept": "application/json",
                    },
                )
                profile_json = api_request.json()
                username = profile_json.get("login", None)
                if username is not None:
                    name = profile_json.get("name")
                    email = profile_json.get("email")
                    bio = profile_json.get("bio")
                    user = models.User.objects.get(email=email)
                    if user is not None:
                        raise GithubException()
                    else :
                        user = models.User.objects.create(
                            username=email, first_name=name, bio=bio, email=email
                        )
                        login(request, user)
                        return redirect(reverse("core:home"))
                else:
                    raise GithubException()

        else:
            raise GithubException()
    except Exception :
        return redirect(reverse("users:login"))


