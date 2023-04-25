# Generated by Django 3.2.15 on 2023-04-17 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_lab_tests'),
    ]

    operations = [
        migrations.CreateModel(
            name='online_consultations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=1000)),
                ('bk_date', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=1000)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.patient')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.doctor')),
            ],
        ),
    ]