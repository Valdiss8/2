# Generated by Django 4.1.2 on 2023-01-10 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tisdac_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=300)),
                ('department', models.CharField(blank=True, default='', max_length=300)),
                ('date', models.DateTimeField()),
                ('description', models.CharField(default='', max_length=10000)),
            ],
        ),
    ]
