# Generated by Django 3.1.5 on 2021-02-07 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_auto_20210207_2111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={},
        ),
        migrations.RemoveField(
            model_name='location',
            name='order_no',
        ),
    ]
