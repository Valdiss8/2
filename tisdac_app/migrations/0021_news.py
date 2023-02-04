# Generated by Django 4.1.2 on 2023-01-19 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tisdac_app', '0020_alter_events_visitors_marker'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=300)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('place', models.CharField(default='Mere pst. 3', max_length=200)),
                ('summary', models.CharField(blank=True, max_length=300, null=True)),
                ('description', models.TextField(null=True)),
                ('slug', models.SlugField(blank=True, default='')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tisdac_app.department')),
                ('visitors', models.ManyToManyField(to='tisdac_app.visitor')),
            ],
        ),
    ]
