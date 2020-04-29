from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


class EmailLoginOnlyView(UserPassesTestMixin):
    # 이메일로 로그인 한 경우에만 handle_no_permission 이 함수를 실행한다.
    def test_func(self):
        return self.request.user.login_method == "email"

    def handle_no_permission(self):
        messages.error(self.request, "Can't go there")
        return redirect("core:home")


class LoggedOutOnlyView(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, "Can't go there")
        return redirect("core:home")


class LoggedInOnlyView(LoginRequiredMixin):
    # 로그인이 되어있지 않은경우 login 페이지로 이동시켜버린다.
    # all requests by non-authenticated users will be redirected to the login page
    # or shown an HTTP 403 Forbidden error, depending on the raise_exception parameter.
    login_url = reverse_lazy("users:login")