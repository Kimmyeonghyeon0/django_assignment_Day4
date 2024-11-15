# Generated by Django 5.0.4 on 2024-11-12 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Todo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="오늘 할일")),
                ("description", models.TextField(max_length=100, verbose_name="본문")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="작성일자"),
                ),
                ("due_date", models.DateTimeField(verbose_name="기간")),
            ],
        ),
    ]
