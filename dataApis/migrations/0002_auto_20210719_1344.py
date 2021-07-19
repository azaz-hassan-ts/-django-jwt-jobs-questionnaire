# Generated by Django 3.2.5 on 2021-07-19 08:44

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataApis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='options',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), blank=True, default=[], size=None),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='type',
            field=models.CharField(choices=[('mcq', 'Multiple Choice Question'), ('numeric', 'Number Based Question'), ('text', 'Text Based Question'), ('code', 'Coding Question')], default='mcq', max_length=10),
        ),
    ]