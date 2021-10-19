# Generated by Django 3.2.6 on 2021-08-12 14:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=40, unique=True, verbose_name='Code coupon')),
                ('valid_from', models.DateTimeField(verbose_name='Valide à partir de')),
                ('valid_to', models.DateTimeField(verbose_name="Valide jusqu'à")),
                ('discount_amount', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Montant')),
                ('discount_percentage', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Pourcentage')),
                ('active', models.BooleanField(default=True, verbose_name='Actif')),
                ('stock', models.IntegerField(default=1, verbose_name='Coupons restant')),
                ('used', models.IntegerField(default=0, verbose_name='Coupons restant')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Date de dernière mise à jour')),
            ],
        ),
    ]
