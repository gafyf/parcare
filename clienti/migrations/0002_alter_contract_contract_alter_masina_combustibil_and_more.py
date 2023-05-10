# Generated by Django 4.0.3 on 2023-05-09 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clienti', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='contract',
            field=models.CharField(blank=True, choices=[(None, 'Selecteaza contract'), ('public', 'Public (500 Lei)'), ('privat', 'Privat (800 Lei)')], max_length=50),
        ),
        migrations.AlterField(
            model_name='masina',
            name='combustibil',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='combustibil'),
        ),
        migrations.AlterField(
            model_name='masina',
            name='culoare',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='culoare'),
        ),
        migrations.AlterField(
            model_name='masina',
            name='marca',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='marca'),
        ),
        migrations.AlterField(
            model_name='masina',
            name='model',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='model'),
        ),
        migrations.AlterField(
            model_name='masina',
            name='numar',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='numar'),
        ),
    ]