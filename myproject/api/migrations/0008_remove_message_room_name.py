# Generated by Django 5.1.2 on 2024-11-26 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='room_name',
        ),
    ]