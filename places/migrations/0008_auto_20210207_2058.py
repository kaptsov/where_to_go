# Generated by Django 3.1.5 on 2021-02-07 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_auto_20210207_1717'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['order_no']},
        ),
        migrations.AlterField(
            model_name='image',
            name='order_no',
            field=models.SmallIntegerField(default=0),
        ),
    ]
