# Generated by Django 1.11.2 on 2017-08-24 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("msgs", "0102_auto_20170725_2129")]

    operations = [migrations.RenameField(model_name="msg", old_name="session", new_name="connection")]