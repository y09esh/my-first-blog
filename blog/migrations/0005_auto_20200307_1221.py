# Generated by Django 3.0.4 on 2020-03-07 06:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200306_1321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='auther',
            new_name='author',
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 7, 6, 50, 58, 657138, tzinfo=utc)),
        ),
    ]
