# Generated by Django 4.0.5 on 2022-07-07 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=100),
        ),
    ]
