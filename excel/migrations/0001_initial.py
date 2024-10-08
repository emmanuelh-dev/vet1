# Generated by Django 5.1 on 2024-09-15 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Covid19Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('symptoms', models.TextField()),
                ('diagnosis_date', models.DateField()),
                ('is_recovered', models.BooleanField(default=False)),
            ],
        ),
    ]
