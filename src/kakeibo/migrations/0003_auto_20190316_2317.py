# Generated by Django 2.0 on 2019-03-16 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kakeibo', '0002_auto_20190316_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_item',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='item',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
