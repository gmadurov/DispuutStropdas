# Generated by Django 4.0.2 on 2022-05-18 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_alter_event_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='summary',
            field=models.CharField(choices=[('Activiteit', 'Activiteit'), ('Borrel', 'Borrel'), ('Clubactiviteit', 'Clubactiviteit'), ('Wedstrijd', 'Wedstrijd'), ('Dispuutsactiviteit', 'Dispuutsactiviteit'), ('Dispuutsverjaardag', 'Dispuutsverjaardag'), ('Dispuutsavonds', 'Dispuutsavonds'), ('AdministratifActivitied', 'AdministratifActivitied'), ('Bier', 'Bier')], max_length=50),
        ),
    ]
