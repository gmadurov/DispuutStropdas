# Generated by Django 4.0.2 on 2022-05-28 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_alter_event_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendaclient',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='nievent',
            name='note',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='nievent',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]