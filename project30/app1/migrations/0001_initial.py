# Generated by Django 5.0.6 on 2024-06-28 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('user', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
