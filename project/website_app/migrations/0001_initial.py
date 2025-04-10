# Generated by Django 5.2 on 2025-04-10 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobTitle', models.CharField(max_length=100)),
                ('jobLocation', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('jobDescription', models.CharField(max_length=500, null=True)),
                ('validThroughDate', models.DateField()),
            ],
        ),
    ]
