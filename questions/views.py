from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from rest_framework import permissions
from questions.serializers import QuestionSerializer
# Create your views here.

class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all().order_by('-vote_up')
    serializer_class = QuestionSerializer
    filterset_fields = ['pinned']

