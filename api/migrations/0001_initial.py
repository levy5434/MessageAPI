# Generated by Django 3.2.3 on 2021-05-20 20:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=160, validators=[django.core.validators.MinLengthValidator(1)])),
                ('views_counter', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
