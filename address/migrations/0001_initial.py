# Generated by Django 4.1.7 on 2023-04-12 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=64)),
                ('street', models.CharField(max_length=128)),
                ('number', models.CharField(max_length=16)),
            ],
        ),
    ]
