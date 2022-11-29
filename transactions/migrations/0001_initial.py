from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Type",
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
                ("descricao", models.CharField(max_length=23)),
                ("natureza", models.CharField(max_length=7)),
                ("sinal", models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name="Transaction",
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
                ("data", models.DateField()),
                ("valor", models.IntegerField()),
                ("cpf", models.CharField(max_length=11)),
                ("cartao", models.CharField(max_length=12)),
                ("hora", models.TimeField()),
                ("dono", models.CharField(max_length=14)),
                ("nome", models.CharField(max_length=19)),
                (
                    "tipo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="transacoes",
                        to="transactions.type",
                    ),
                ),
            ],
        ),
    ]
