# Generated by Django 2.1 on 2018-08-15 08:55

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0021_auto_20180815_1153"),
    ]

    operations = [
        migrations.AddField(
            model_name="volunteer",
            name="joined",
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
