# Generated by Django 4.1.7 on 2023-11-08 03:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_test_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 18, 3, 23, 41, 23912, tzinfo=datetime.timezone.utc)),
        ),
    ]
