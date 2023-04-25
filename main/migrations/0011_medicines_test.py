# Generated by Django 3.2.15 on 2023-04-04 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_user_image_prescription'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(max_length=1000)),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.prescription')),
            ],
        ),
        migrations.CreateModel(
            name='medicines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine', models.CharField(max_length=50)),
                ('freequency', models.CharField(max_length=1000)),
                ('dosage', models.CharField(max_length=50)),
                ('med_duration', models.CharField(max_length=50)),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.prescription')),
            ],
        ),
    ]