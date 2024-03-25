# Generated by Django 5.0.2 on 2024-03-25 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescription', '0004_appointment_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='confirmed',
            field=models.BooleanField(default=False, help_text='True if the appointment is confirmed'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.BooleanField(default=False, help_text='false if the appointment is Pending'),
        ),
    ]
