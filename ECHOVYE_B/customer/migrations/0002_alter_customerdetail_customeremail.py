# Generated by Django 3.2.5 on 2021-07-21 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdetail',
            name='CustomerEmail',
            field=models.EmailField(max_length=55),
        ),
    ]
