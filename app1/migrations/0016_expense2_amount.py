# Generated by Django 4.0.4 on 2022-11-26 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_expense2'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense2',
            name='amount',
            field=models.IntegerField(null=True),
        ),
    ]
