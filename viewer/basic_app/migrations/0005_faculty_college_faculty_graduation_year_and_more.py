# Generated by Django 4.0.3 on 2022-11-17 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0004_alter_faculty_aadhar_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='college',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='faculty',
            name='graduation_year',
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AddField(
            model_name='faculty',
            name='percentage',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='faculty',
            name='qualification',
            field=models.CharField(blank=True, choices=[('SSC', 'SSC'), ('Inter', 'Inter'), ('UG', 'UG'), ('PG', 'PG'), ('Phd', 'Phd'), ('Others', 'Others')], max_length=25),
        ),
        migrations.AddField(
            model_name='faculty',
            name='university',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
