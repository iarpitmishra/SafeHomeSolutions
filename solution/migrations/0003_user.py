# Generated by Django 4.2.3 on 2023-08-12 10:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('solution', '0002_alter_employee_type_charge_permonth_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=45)),
                ('userpass', models.CharField(max_length=45)),
                ('name', models.CharField(max_length=45)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=45)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
