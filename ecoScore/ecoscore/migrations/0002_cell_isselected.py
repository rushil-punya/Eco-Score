# Generated by Django 3.0.6 on 2020-08-28 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecoscore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cell',
            name='isSelected',
            field=models.BooleanField(default=False),
        ),
    ]