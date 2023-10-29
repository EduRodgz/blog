# Generated by Django 4.2.6 on 2023-10-27 00:45

from django.db import migrations

def populate_status(apps, schemaeditor):
    entries = {
        "published": "A post that is visible to all.",
        "draft": "A post only the author can see.",
        "archived": "A post only visible to logged in users."
    }
    Status = apps.get_model("posts", "Status")
    for key, value in entries.items():
        status_obj = Status(name=key, description=value)
        status_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_status_post_status'),
    ]

    operations = [
        migrations.RunPython(populate_status)
    ]