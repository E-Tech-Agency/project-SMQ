# Generated by Django 5.0.3 on 2024-05-23 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0009_alter_demanddocument_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demanddocument',
            name='is_validated',
        ),
        migrations.AddField(
            model_name='demanddocument',
            name='statut',
            field=models.CharField(choices=[('En attente', 'En attente'), ('Validé', 'Validé'), ('Refusé', 'Refusé'), ('terminé', 'terminé')], default='En attente', max_length=20),
        ),
    ]