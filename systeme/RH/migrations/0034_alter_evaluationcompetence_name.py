# Generated by Django 5.0.3 on 2024-06-06 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RH', '0033_remove_planaction_evaluation_planaction_competence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluationcompetence',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]