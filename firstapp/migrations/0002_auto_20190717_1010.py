# Generated by Django 2.2.3 on 2019-07-17 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='Account_Number',
            field=models.IntegerField(),
        ),
    ]
