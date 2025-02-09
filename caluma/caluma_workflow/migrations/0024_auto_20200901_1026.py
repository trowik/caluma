# Generated by Django 2.2.15 on 2020-09-01 10:26

from django.db import migrations

import caluma.caluma_core.models


class Migration(migrations.Migration):

    dependencies = [("caluma_workflow", "0023_auto_20200730_1135")]

    operations = [
        migrations.AlterField(
            model_name="case",
            name="status",
            field=caluma.caluma_core.models.ChoicesCharField(
                choices=[
                    ("running", "Case is running and work items need to be completed."),
                    ("completed", "Case is done."),
                    ("canceled", "Case is cancelled."),
                    ("suspended", "Case is suspended."),
                ],
                db_index=True,
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="historicalcase",
            name="status",
            field=caluma.caluma_core.models.ChoicesCharField(
                choices=[
                    ("running", "Case is running and work items need to be completed."),
                    ("completed", "Case is done."),
                    ("canceled", "Case is cancelled."),
                    ("suspended", "Case is suspended."),
                ],
                db_index=True,
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="historicalworkitem",
            name="status",
            field=caluma.caluma_core.models.ChoicesCharField(
                choices=[
                    ("ready", "Task is ready to be processed."),
                    ("completed", "Task is done."),
                    ("canceled", "Task is cancelled."),
                    ("skipped", "Task is skipped."),
                    ("suspended", "Task is suspended."),
                ],
                db_index=True,
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="workitem",
            name="status",
            field=caluma.caluma_core.models.ChoicesCharField(
                choices=[
                    ("ready", "Task is ready to be processed."),
                    ("completed", "Task is done."),
                    ("canceled", "Task is cancelled."),
                    ("skipped", "Task is skipped."),
                    ("suspended", "Task is suspended."),
                ],
                db_index=True,
                max_length=50,
            ),
        ),
    ]
