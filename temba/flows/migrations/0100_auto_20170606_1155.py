# Generated by Django 1.10.5 on 2017-06-06 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("flows", "0099_populate_recent_message")]

    operations = [
        migrations.RemoveField(model_name="flowpathrecentstep", name="step"),
        migrations.DeleteModel(name="FlowPathRecentStep"),
    ]