# Generated by Django 4.0.3 on 2023-02-21 15:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('useri', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Masina',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('p_json', models.JSONField(blank=True, default=dict, null=True)),
                ('marca', models.CharField(blank=True, max_length=20, null=True)),
                ('model', models.CharField(blank=True, max_length=20, null=True)),
                ('numar', models.CharField(blank=True, max_length=20, null=True)),
                ('culoare', models.CharField(blank=True, max_length=20, null=True)),
                ('combustibil', models.CharField(blank=True, max_length=20, null=True)),
                ('data_creare', models.DateTimeField(auto_now_add=True)),
                ('profil', models.ManyToManyField(related_name='masini', to='useri.profil')),
            ],
            options={
                'verbose_name_plural': 'Masini',
                'ordering': ['-data_creare'],
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('data_creare', models.DateTimeField(auto_now_add=True)),
                ('data_expirare', models.DateTimeField(default=django.utils.timezone.now)),
                ('platit', models.BooleanField(default=False)),
                ('contract', models.CharField(blank=True, choices=[(None, 'Selecteaza contract'), ('public', 'public'), ('privat', 'privat')], max_length=50)),
                ('numar', models.PositiveIntegerField(default=0)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='contracte_clienti/')),
                ('profil', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contracts', to='useri.profil')),
            ],
            options={
                'verbose_name_plural': 'Contracte',
                'ordering': ['-data_creare'],
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nr_permis', models.CharField(blank=True, max_length=20, null=True)),
                ('categ_permis', models.CharField(blank=True, max_length=20, null=True)),
                ('data_creare', models.DateTimeField(auto_now_add=True)),
                ('profil', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='useri.profil')),
            ],
            options={
                'verbose_name_plural': 'Clienti',
                'ordering': ['-data_creare'],
            },
        ),
    ]
