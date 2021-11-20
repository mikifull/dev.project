# Generated by Django 3.2.9 on 2021-11-20 19:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('oauth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('betting', models.FloatField()),
                ('join_date', models.DateTimeField(auto_now_add=True)),
                ('live_date', models.DateTimeField(default=datetime.date(2021, 11, 24))),
                ('better', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserBettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bettings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oauth.authuser')),
            ],
        ),
        migrations.CreateModel(
            name='Bettingsdesc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('meta_name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=2000)),
                ('meta_description', models.CharField(max_length=150)),
                ('keyboards', models.CharField(max_length=200)),
                ('bettings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bettings.bettings')),
            ],
        ),
    ]