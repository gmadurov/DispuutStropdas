# Generated by Django 4.0.2 on 2022-03-05 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_lid_initials'),
        ('agenda', '0007_alter_nievent_options_alter_event_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendaclient',
            name='lid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.lid'),
        ),
    ]
