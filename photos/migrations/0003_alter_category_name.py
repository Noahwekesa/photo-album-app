# Generated by Django 4.2.9 on 2024-02-14 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_photo_slug_alter_photo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
