# Generated by Django 4.0.2 on 2022-05-19 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_alter_document_senate_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='senate_year',
            field=models.IntegerField(default=32),
        ),
    ]
