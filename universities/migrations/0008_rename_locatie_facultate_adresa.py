# Generated by Django 5.1.6 on 2025-03-08 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("universities", "0007_alter_program_options"),
    ]

    operations = [
        migrations.RenameField(
            model_name="facultate",
            old_name="locatie",
            new_name="adresa",
        ),
    ]
