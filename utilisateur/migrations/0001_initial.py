# Generated by Django 3.1.2 on 2022-04-19 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_complet', models.CharField(max_length=200, null=True)),
                ('num_telephone', models.CharField(max_length=200, null=True)),
                ('e_mail', models.EmailField(max_length=200, null=True)),
            ],
        ),
    ]
