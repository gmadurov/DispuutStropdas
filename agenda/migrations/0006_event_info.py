# Generated by Django 4.0.2 on 2022-05-29 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0005_alter_event_bijzonderheden'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='info',
            field=models.TextField(blank=True, null=True),
        ),
    ]
