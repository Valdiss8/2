# Generated by Django 4.1.2 on 2023-01-24 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tisdac_app', '0036_feedback_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='feedback',
            field=models.CharField(max_length=3000, null=True),
        ),
    ]
