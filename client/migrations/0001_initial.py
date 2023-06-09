# Generated by Django 4.1.7 on 2023-04-30 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=60, verbose_name="Nome")),
                ("cpf", models.CharField(max_length=14, verbose_name="CPF")),
                ("phone", models.CharField(max_length=14, verbose_name="Telefone")),
                ("address", models.CharField(max_length=100, verbose_name="Endereço")),
            ],
        ),
    ]
