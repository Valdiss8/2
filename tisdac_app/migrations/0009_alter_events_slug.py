# Generated by Django 4.1.2 on 2023-01-10 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tisdac_app', '0008_events_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]
