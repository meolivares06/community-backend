# Generated by Django 3.1.7 on 2021-02-21 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='comments_qt',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
