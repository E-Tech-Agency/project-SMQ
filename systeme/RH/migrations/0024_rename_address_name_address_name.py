# Generated by Django 5.0.3 on 2024-05-11 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RH', '0023_alter_formation_participants'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='address_name',
            new_name='name',
        ),
    ]