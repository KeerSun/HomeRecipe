# Generated by Django 2.2 on 2020-05-11 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20200511_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='introduction',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
