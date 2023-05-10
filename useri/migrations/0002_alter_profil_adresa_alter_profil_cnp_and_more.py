# Generated by Django 4.0.3 on 2023-05-09 09:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import useri.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('useri', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='adresa',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Adresa'),
        ),
        migrations.AlterField(
            model_name='profil',
            name='cnp',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='CNP'),
        ),
        migrations.AlterField(
            model_name='profil',
            name='data_creare',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data creare'),
        ),
        migrations.AlterField(
            model_name='profil',
            name='imagine',
            field=models.ImageField(blank=True, null=True, upload_to=useri.models.user_directory_path, verbose_name='Imagine'),
        ),
        migrations.AlterField(
            model_name='profil',
            name='judet',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Judet'),
        ),
        migrations.AlterField(
            model_name='profil',
            name='nume',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nume'),
        ),
        migrations.AlterField(
            model_name='profil',
            name='oras',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Oras'),
        ),
        migrations.AlterField(
            model_name='profil',
            name='prenume',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Prenume'),
        ),
        migrations.AlterField(
            model_name='profil',
            name='telefon',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefon'),
        ),
        migrations.AlterField(
            model_name='profil',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Utilizator'),
        ),
    ]
