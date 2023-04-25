# Generated by Django 3.2.15 on 2023-03-24 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_lab_labs'),
    ]

    operations = [
        migrations.CreateModel(
            name='upload_pharmacy_prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amt', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.patient')),
                ('pharmacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.pharmacy')),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.prescription')),
            ],
        ),
        migrations.CreateModel(
            name='medicine_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=100)),
                ('rate', models.CharField(max_length=100)),
                ('total', models.CharField(max_length=100)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.medicine')),
                ('upload_pharmacy_prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.upload_pharmacy_prescription')),
            ],
        ),
    ]
