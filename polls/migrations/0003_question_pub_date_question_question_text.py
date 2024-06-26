# Generated by Django 5.0.6 on 2024-05-29 11:36

import datetime
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0002_remove_question_pub_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="pub_date",
            field=models.DateTimeField(
                blank=True,
                default=django.utils.timezone.now,
                verbose_name="date published",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="question",
            name="question_text",
            field=models.CharField(
                default=datetime.datetime(
                    2024, 5, 29, 11, 36, 18, 479060, tzinfo=datetime.timezone.utc
                ),
                max_length=200,
            ),
            preserve_default=False,
        ),
    ]
