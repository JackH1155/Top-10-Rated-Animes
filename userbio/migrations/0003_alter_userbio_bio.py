# Generated by Django 4.2.16 on 2024-09-24 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userbio', '0002_userbio_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbio',
            name='bio',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]
