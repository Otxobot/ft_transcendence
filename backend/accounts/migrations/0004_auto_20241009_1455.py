# Generated by Django 3.1.7 on 2024-10-09 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20241009_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otptoken',
            name='otp_code',
            field=models.CharField(default='57a77c', max_length=6),
        ),
    ]
