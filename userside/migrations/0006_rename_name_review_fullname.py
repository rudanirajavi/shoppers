# Generated by Django 4.2.4 on 2024-01-09 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0005_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='name',
            new_name='fullname',
        ),
    ]
