# Generated by Django 3.2.5 on 2021-07-11 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer_Detail',
            new_name='CustomerDetail',
        ),
    ]
