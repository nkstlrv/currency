# Generated by Django 4.2.3 on 2023-07-03 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0002_rename_contactus_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
    ]