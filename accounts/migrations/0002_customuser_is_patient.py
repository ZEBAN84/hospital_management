# Generated by Django 3.2.12 on 2024-08-04 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_patient',
            field=models.BooleanField(default=False),
        ),
    ]
