# Generated by Django 5.1.6 on 2025-03-08 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("universities", "0006_remove_facultate_materii_program_materii"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="program",
            options={"verbose_name_plural": "programe"},
        ),
    ]
