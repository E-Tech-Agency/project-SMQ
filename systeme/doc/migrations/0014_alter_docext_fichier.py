# Generated by Django 5.0.3 on 2024-05-27 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0013_delete_activite_delete_site_delete_type_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docext',
            name='fichier',
            field=models.FileField(blank=True, null=True, upload_to='documentsExt/'),
        ),
    ]