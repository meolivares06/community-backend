from django.db import models
from model_utils.fields import AutoCreatedField, AutoLastModifiedField
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Question(models.Model):
    title = models.CharField(_('title'), max_length=200)
    category = models.CharField(_('category'), max_length=200)
    username = models.CharField(_('username'), max_length=200)
    pinned = models.BooleanField(_('pinned'), default=False)
    grade = models.CharField(_('grade'), max_length=200)
    description = models.TextField(default=None, blank=True, null=True)
    vote_up = models.IntegerField(default=0)
    comments_qt = models.IntegerField(default=0)
    vote_down = models.IntegerField(default=0)
    created = AutoCreatedField('created')
    updated = AutoLastModifiedField('modified')

    def __str__(self):
        return self.title
