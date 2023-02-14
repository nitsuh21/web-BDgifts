# Generated by Django 3.0.5 on 2020-11-24 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('emailed', models.IntegerField(default=0)),
                ('gift', models.CharField(max_length=100000, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('gifttype', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('url', models.URLField(max_length=100000, null=True)),
                ('message', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('message', models.CharField(max_length=100000, null=True)),
                ('relation', models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]