# Generated by Django 4.2.4 on 2024-01-09 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0007_rename_email_review_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='comment',
            field=models.CharField(default=2, max_length=300),
            preserve_default=False,
        ),
    ]
