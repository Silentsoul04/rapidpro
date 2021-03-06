# Generated by Django 1.11.6 on 2018-05-15 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("archives", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="archive",
            name="archive_type",
            field=models.CharField(
                choices=[("messages", "Message"), ("runs", "Run")],
                help_text="The type of record this is an archive for",
                max_length=16,
            ),
        )
    ]
