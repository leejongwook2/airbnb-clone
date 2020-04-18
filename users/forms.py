from django import forms
from . import models

class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


    # validation 체크 하고싶으면 valid_필드이름 이어야 한데
    # 이 함수에서 값이 있나 체크를 하는거구나 .. ㅇㅇ
    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))


class SignUpForm(forms.ModelForm):

    # 이 Model Form 이라는게 clena_ 해준다고 함...
    class Meta:
        model = models.User
        fields = ("first_name", "last_name", "email")

    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")

        if password != password1:
            raise forms.ValidationError("Pasword confirmations does not match")
        else :
            return password

    def save(self, *args, **kwargs):
        user = super().save(commit=False) # Call the real save() method
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user.username = email
        # 이거 않하면 패스워드 세팅이 안되버리네 .... ㅇㅇ
        user.set_password(password)
        user.save()

