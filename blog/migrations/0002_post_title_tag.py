# Generated by Django 3.2 on 2022-03-06 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Habitite Blog', max_length=255),
        ),
    ]