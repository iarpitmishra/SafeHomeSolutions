# Generated by Django 4.2.3 on 2023-08-12 10:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('solution', '0006_query'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offers_Scheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offercontents', models.CharField(max_length=45)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
