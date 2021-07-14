# Generated by Django 3.2.5 on 2021-07-11 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Detail',
            fields=[
                ('CustomerName', models.CharField(max_length=100)),
                ('Customer_Id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('Address', models.TextField(blank=True, null=True)),
                ('Email', models.EmailField(max_length=55, unique=True)),
                ('Contact_1', models.CharField(max_length=10)),
                ('Contact_2', models.CharField(blank=True, max_length=10, null=True)),
                ('Date', models.CharField(max_length=30)),
                ('Location', models.TextField(blank=True, null=True)),
            ],
        ),
    ]