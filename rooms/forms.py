from django import forms
from django_countries.fields import CountryField
from . import models

class SearchForm(forms.Form):
    # wiget 은 HTML ELEMENT 야. .. 요소인거지
    city = forms.CharField(max_length=120, initial="AnyWhere")
    country = CountryField(default="KR").formfield()
    room_type = forms.ModelChoiceField(empty_label="Any Kind", required=False ,queryset=models.RoomType.objects.all())
    price = forms.IntegerField(required=False)
    guests = forms.IntegerField(required=False)
    bedrooms = forms.IntegerField(required=False)
    beds = forms.IntegerField(required=False)
    baths = forms.IntegerField(required=False)
    instant_book = forms.BooleanField(required=False)
    superhost = forms.BooleanField(required=False)
    amenities = forms.ModelMultipleChoiceField(required=False, queryset=models.Amenity.objects.all(), widget=forms.CheckboxSelectMultiple)
    facilities = forms.ModelMultipleChoiceField(required=False, queryset=models.Facility.objects.all(), widget=forms.CheckboxSelectMultiple)
