# Generated by Django 4.2.3 on 2023-07-04 15:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("currency", "0006_alter_rates_currency"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rates",
            name="source",
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
