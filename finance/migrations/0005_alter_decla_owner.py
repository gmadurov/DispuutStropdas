# Generated by Django 4.0.2 on 2022-05-30 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_lid_active_alter_lid_initials'),
        ('finance', '0004_alter_decla_present'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decla',
            name='owner',
            field=models.ForeignKey(default=19900, on_delete=django.db.models.deletion.CASCADE, to='users.lid'),
        ),
    ]