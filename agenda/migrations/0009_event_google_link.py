# Generated by Django 4.0.2 on 2022-03-05 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0008_alter_agendaclient_lid'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='google_link',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]