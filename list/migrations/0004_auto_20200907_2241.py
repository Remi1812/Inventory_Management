# Generated by Django 3.0.7 on 2020-09-07 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_customer_master_sale'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='raw_data',
            new_name='purchase',
        ),
        migrations.AlterField(
            model_name='product_master',
            name='pname',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]