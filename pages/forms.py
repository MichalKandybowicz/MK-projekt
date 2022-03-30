from django.core.exceptions import ValidationError
from django.forms import ModelForm

from backend.models import Movie

baned_words_list = ['dupa', 'Dupa', ]


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title']

    def __init__(self, *args, **kwargs):
        super(MovieForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Dodaj film wisując jego tytuł"

    def clean_title(self):
        data = self.cleaned_data['title']
        if data is None:
            raise ValidationError("Bez tytułu nie da rady :(")
        elif Movie.objects.filter(title=data).exists():
            raise ValidationError("Ten film istnieje już w naszej bazie :)")
        elif data in baned_words_list:
            raise ValidationError("Proszę bez brzydkich słów")
        return data