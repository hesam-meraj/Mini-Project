# Generated by Django 5.1 on 2024-09-01 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_management', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publish_at',
            new_name='published_at',
        ),
    ]
