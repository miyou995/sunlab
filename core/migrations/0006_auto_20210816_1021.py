# Generated by Django 3.2.6 on 2021-08-16 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_product_gamme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='utilisation',
        ),
        migrations.AlterField(
            model_name='product',
            name='photo1',
            field=models.ImageField(default=2, upload_to='images/produits'),
            preserve_default=False,
        ),
    ]
