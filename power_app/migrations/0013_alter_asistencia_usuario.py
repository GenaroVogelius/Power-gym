# Generated by Django 4.2.1 on 2023-05-13 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("power_app", "0012_asistencia"),
    ]

    operations = [
        migrations.AlterField(
            model_name="asistencia",
            name="usuario",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="power_app.usuario"
            ),
        ),
    ]
