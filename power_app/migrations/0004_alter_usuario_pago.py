# Generated by Django 4.2 on 2023-04-14 19:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("power_app", "0003_alter_usuario_pago"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuario",
            name="pago",
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
