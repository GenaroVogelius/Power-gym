# Generated by Django 4.2.1 on 2023-05-13 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("power_app", "0013_alter_asistencia_usuario"),
    ]

    operations = [
        migrations.AddField(
            model_name="asistencia",
            name="activo",
            field=models.BooleanField(default=True, editable=False),
        ),
    ]
