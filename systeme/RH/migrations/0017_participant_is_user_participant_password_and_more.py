# Generated by Django 5.0.3 on 2024-04-11 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RH', '0016_employe_is_user_employe_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='is_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='participant',
            name='password',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='responsableformation',
            name='is_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='responsableformation',
            name='password',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
    ]