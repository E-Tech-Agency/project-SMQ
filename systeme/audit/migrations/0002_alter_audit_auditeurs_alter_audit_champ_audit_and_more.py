# Generated by Django 5.0.3 on 2024-04-22 10:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='audit',
            name='auditeurs',
            field=models.ManyToManyField(related_name='audits_auditors', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='audit',
            name='champ_audit',
            field=models.ManyToManyField(related_name='audits_access', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='audit',
            name='responsable_validation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audits_validator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='planaudit',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_audit_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='planaudit',
            name='personnes_concernees',
            field=models.ManyToManyField(related_name='personnes_concernees', to=settings.AUTH_USER_MODEL),
        ),
    ]