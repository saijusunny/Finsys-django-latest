# Generated by Django 4.0.4 on 2022-11-11 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
