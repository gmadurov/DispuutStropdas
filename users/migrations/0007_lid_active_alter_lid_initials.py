# Generated by Django 4.0.2 on 2022-05-20 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_lid_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='lid',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='lid',
            name='initials',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]