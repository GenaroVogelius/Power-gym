# Generated by Django 4.2 on 2023-04-14 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("power_app", "0002_usuario_vencimiento"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuario",
            name="pago",
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
