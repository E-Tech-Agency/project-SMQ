# Generated by Django 5.0.3 on 2024-06-06 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indicateur', '0007_alter_historicalindicateur_axe_politique_qualite_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suiviindicateur',
            name='liste',
        ),
    ]