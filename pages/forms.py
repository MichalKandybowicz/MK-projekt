from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ModelForm, Form
from django import forms
from accounts.models import CustomUser
from django.utils.translation import ugettext_lazy as _


