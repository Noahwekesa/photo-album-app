# Generated by Django 4.2.9 on 2024-03-01 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("photos", "0004_alter_category_options_alter_category_name"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="photo",
            options={"verbose_name": "Photo", "verbose_name_plural": "Photos"},
        ),
        migrations.RemoveField(
            model_name="photo",
            name="created",
        ),
        migrations.RemoveField(
            model_name="photo",
            name="modified",
        ),
        migrations.RemoveField(
            model_name="photo",
            name="slug",
        ),
        migrations.RemoveField(
            model_name="photo",
            name="title",
        ),
        migrations.RemoveField(
            model_name="photo",
            name="user",
        ),
        migrations.AlterField(
            model_name="photo",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
