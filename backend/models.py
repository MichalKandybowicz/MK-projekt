from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse

from accounts.models import CustomUser
from django.utils.translation import ugettext_lazy as _
from accounts.models import CustomUser


class Potion(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    # bonus = odniesienie do efektu

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('author-detail-view', args=[str(self.id)])


class Monster(models.Model):
    name = models.CharField(max_length=50)
    # description = models.ForeignKey(MonsterType, related_name="book_type", on_delete=modelsls.PROTECT)
    # monster_type = models.ForeignKey(BookType, related_name="book_type", on_delete=models.PROTECT)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('book-detail-view', args=[str(self.id)])


class MonsterType(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    votes = models.IntegerField(default=0)
    date_of_publication = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('movie-detail-view', args=[str(self.id)])



