# Generated by Django 5.0.6 on 2024-07-10 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=50)),
                ('nom', models.CharField(max_length=50)),
                ('adresse', models.EmailField(max_length=50)),
                ('ville', models.CharField(max_length=50)),
                ('pays', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=50)),
                ('date_commande', models.DateTimeField()),
            ],
            options={
                'ordering': ['-date_commande'],
            },
        ),
    ]
