# Generated by Django 4.2.4 on 2023-08-04 14:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("currency", "0003_alter_rate_source"),
    ]

    operations = [
        migrations.AddField(
            model_name="source",
            name="logo",
            field=models.FileField(default=None, null=True, upload_to=""),
        ),
    ]
