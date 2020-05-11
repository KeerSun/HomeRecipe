# Generated by Django 2.2 on 2020-05-11 17:55

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_auto_20200511_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='instructionsImg',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(upload_to='images/'), default=None, size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='instructionsTxt',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=None, size=None),
            preserve_default=False,
        ),
    ]
