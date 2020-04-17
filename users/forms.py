from django import forms
from . import models

class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


    # validation 체크 하고싶으면 valid_필드이름 이어야 한데
    # 이 함수에서 값이 있나 체크를 하는거구나 .. ㅇㅇ
    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("passwrd")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))