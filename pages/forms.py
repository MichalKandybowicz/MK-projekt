from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ModelForm, Form
from django import forms
from accounts.models import CustomUser
from django.utils.translation import ugettext_lazy as _

from backend.models import Movie


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title']

    def __init__(self, *args, **kwargs):
        super(MovieForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Tytuł"

    def clean_title(self):
        data = self.cleaned_data['title']
        if Movie.objects.filter(title=data).exists():
            raise ValidationError("Mamy juz w bazie taki film :)")
        if data == None:
            raise ValidationError("Bez tytułu nie da rady :(")

        return data
