# Generated by Django 5.1.3 on 2024-12-08 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_users', '0002_telegramusers_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramusers',
            name='language',
            field=models.CharField(choices=[('ru', 'Ru'), ('uz', 'Uz')], default='uz', max_length=2),
        ),
    ]
