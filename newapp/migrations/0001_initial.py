# Generated by Django 4.2.13 on 2024-06-07 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('centername', models.CharField(max_length=100)),
            ],
        ),
    ]
