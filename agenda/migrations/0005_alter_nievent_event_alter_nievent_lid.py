# Generated by Django 4.0.2 on 2022-03-03 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_lid_initials'),
        ('agenda', '0004_alter_event_options_alter_nievent_event_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nievent',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dsani_ev', to='agenda.event'),
        ),
        migrations.AlterField(
            model_name='nievent',
            name='lid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.lid'),
        ),
    ]
