# Generated by Django 1.11.6 on 2018-03-22 18:55

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("flows", "0147_new_engine_changes")]

    operations = [
        migrations.AddField(
            model_name="flowrun",
            name="events",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                help_text="The events recorded on this run in JSON format", null=True, verbose_name="Fields"
            ),
        )
    ]