# Generated by Django 5.0.2 on 2024-03-25 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescription', '0005_appointment_confirmed_alter_appointment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(),
        ),
    ]