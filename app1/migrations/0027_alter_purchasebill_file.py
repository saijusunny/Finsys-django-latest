# Generated by Django 4.0.4 on 2022-11-08 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0026_alter_purchasepayment1_duedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasebill',
            name='file',
            field=models.FileField(default='default.jpg', upload_to='purchase/bill'),
        ),
    ]
