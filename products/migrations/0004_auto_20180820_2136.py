# Generated by Django 2.0.6 on 2018-08-20 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20180820_2021'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='category',
        ),
    ]
