# Generated by Django 4.2.4 on 2024-01-09 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0010_rename_user_email_usersidereview_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserSideReview',
            new_name='review',
        ),
    ]
