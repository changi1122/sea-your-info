# Generated by Django 3.0.5 on 2020-05-16 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_userprofile_hassubscribed'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='hasSubscribed',
            field=models.BooleanField(default=False),
        ),
    ]
