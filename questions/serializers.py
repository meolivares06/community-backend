from django.contrib.auth.models import User, Group
from .models import Question
from rest_framework import serializers


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'title', 'description', 'category', 'username', 'pinned', 'grade', 'description', 'vote_up', 'vote_down', 'created', 'updated', 'comments_qt']


