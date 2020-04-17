from django import forms
from . import models

class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


    # validation 체크 하고싶으면 valid_필드이름 이어야 한데
    # 이 함수에서 값이 있나 체크를 하는거구나 .. ㅇㅇ
    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(username=email)
            return email
        except models.User.DoesNotExist:
            raise forms.ValidationError("User does not exist")

    def clean_password(self):
        return "fsjfojsjo"
