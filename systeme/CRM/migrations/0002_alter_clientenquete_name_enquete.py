# Generated by Django 5.0.3 on 2024-05-31 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientenquete',
            name='name_enquete',
            field=models.CharField(default='Nom par défaut', max_length=255, unique=True),
        ),
    ]