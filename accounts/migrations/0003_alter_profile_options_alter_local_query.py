# Generated by Django 4.0.4 on 2022-07-18 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_options_remove_profile_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Perfil', 'verbose_name_plural': 'Perfiles'},
        ),
        migrations.AlterField(
            model_name='local',
            name='query',
            field=models.IntegerField(blank=True, choices=[[0, 'PetShop'], [1, 'Veterinaria'], [2, 'Paseador/Recreación'], [3, 'Guardería'], [4, 'Peluquería']], default=0),
        ),
    ]
