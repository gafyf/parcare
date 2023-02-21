# Generated by Django 4.0.3 on 2023-02-21 15:25

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('useri', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('functie', models.CharField(blank=True, choices=[(None, 'Selecteaza functie'), ('paznic', 'paznic'), ('electrician', 'electrician'), ('casier', 'casier'), ('secretara', 'secretara'), ('director', 'director')], max_length=50, null=True)),
                ('data_angajarii', models.DateTimeField(auto_now_add=True)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='contracte_staff/')),
                ('numar', models.PositiveIntegerField(default=0)),
                ('profil', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='useri.profil')),
            ],
            options={
                'verbose_name_plural': 'Staff',
                'ordering': ['-data_angajarii'],
            },
        ),
    ]