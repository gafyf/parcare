# Generated by Django 4.0.3 on 2023-05-09 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plati', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='card_number',
            field=models.CharField(max_length=16, verbose_name='Numar Card'),
        ),
        migrations.AlterField(
            model_name='card',
            name='cvc',
            field=models.CharField(max_length=3, verbose_name='CVC'),
        ),
        migrations.AlterField(
            model_name='card',
            name='expiration_month',
            field=models.CharField(max_length=2, verbose_name='Luna Expirare'),
        ),
        migrations.AlterField(
            model_name='card',
            name='expiration_year',
            field=models.CharField(max_length=2, verbose_name='An Expirare'),
        ),
        migrations.AlterField(
            model_name='card',
            name='name',
            field=models.CharField(default='', max_length=100, verbose_name='Posesor Card'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='data_creare',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data creare'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='numar',
            field=models.PositiveIntegerField(default=0, verbose_name='Numar'),
        ),
    ]
