# Generated by Django 3.2.12 on 2022-03-24 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("caluma_analytics", "0001_initial"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="analyticsfield",
            name="unique_data_source",
        ),
        migrations.AddField(
            model_name="analyticsfield",
            name="function",
            field=models.CharField(
                choices=[
                    ("value", "Plain value (Implies GROUP BY)"),
                    ("sum", "Sum"),
                    ("count", "Count"),
                    ("avg", "Average (Mean)"),
                    ("max", "Max"),
                    ("min", "Min"),
                ],
                default="value",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="analyticsfield",
            name="show_output",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="historicalanalyticsfield",
            name="function",
            field=models.CharField(
                choices=[
                    ("value", "Plain value (Implies GROUP BY)"),
                    ("sum", "Sum"),
                    ("count", "Count"),
                    ("avg", "Average (Mean)"),
                    ("max", "Max"),
                    ("min", "Min"),
                ],
                default="value",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="historicalanalyticsfield",
            name="show_output",
            field=models.BooleanField(default=True),
        ),
        migrations.AddConstraint(
            model_name="analyticsfield",
            constraint=models.UniqueConstraint(
                fields=("table", "data_source", "function"), name="unique_data_source"
            ),
        ),
    ]
