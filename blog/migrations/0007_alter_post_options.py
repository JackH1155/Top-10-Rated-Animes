# Generated by Django 4.2.16 on 2024-09-20 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_options_post_rating_alter_post_created_on_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['rating']},
        ),
    ]