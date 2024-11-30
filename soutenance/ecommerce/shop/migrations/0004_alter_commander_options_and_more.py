# Generated by Django 5.0.6 on 2024-07-10 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_commander_delete_commande'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commander',
            options={'ordering': ['-date_commander']},
        ),
        migrations.RemoveField(
            model_name='commander',
            name='date_commande',
        ),
        migrations.AddField(
            model_name='commander',
            name='date_commander',
            field=models.DateTimeField(auto_now=True),
        ),
    ]