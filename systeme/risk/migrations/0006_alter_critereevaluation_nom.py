# Generated by Django 5.0.3 on 2024-06-01 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk', '0005_alter_critereevaluation_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='critereevaluation',
            name='nom',
            field=models.CharField(choices=[('Probabilité occurrence', 'Probabilité occurrence'), ('Impact', 'Impact'), ('Vulnérabilité', 'Vulnérabilité'), ('Mesures de contrôle existantes', 'Mesures de contrôle existantes'), ('Capacité de détection', 'Capacité de détection'), ('Tendance ', 'Tendance ')]),
        ),
    ]
