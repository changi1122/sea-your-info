# Generated by Django 3.0.5 on 2020-05-17 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200517_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='topics',
            field=models.TextField(default=''),
        ),
    ]