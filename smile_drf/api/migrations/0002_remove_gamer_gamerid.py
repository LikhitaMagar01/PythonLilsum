# Generated by Django 4.1.3 on 2022-12-05 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamer',
            name='gamerid',
        ),
    ]
