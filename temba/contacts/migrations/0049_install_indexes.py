# Generated by Django 1.10.5 on 2017-01-13 07:24

from django.db import migrations


class Migration(migrations.Migration):

    INDEX_SQL = """
CREATE INDEX org_test_contacts
ON contacts_contact (org_id) WHERE is_test = TRUE;

CREATE INDEX contacts_contact_org_modified_id_where_nontest_active
ON contacts_contact (org_id, modified_on DESC, id DESC)
WHERE is_test = false AND is_active = true;

CREATE INDEX contacts_contact_org_modified_id_where_nontest_inactive
ON contacts_contact (org_id, modified_on DESC, id DESC)
WHERE is_test = false AND is_active = false;
    """

    dependencies = [("contacts", "0048_install_triggers")]

    operations = [migrations.RunSQL(INDEX_SQL)]