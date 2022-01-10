from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

from accounts.models import CustomUser
import uuid
import random
import string

# from backend.models import Author, BookType, Book
# from backend.serializers import AuthorSerializer, BookTypeSerializer, BookSerializer
