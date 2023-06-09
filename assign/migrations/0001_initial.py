# Generated by Django 4.2.1 on 2023-05-23 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('resource', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assigned',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_id', models.CharField(max_length=50)),
                ('assign_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='addBillable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resource.details')),
            ],
        ),
        migrations.CreateModel(
            name='addAssigned',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assign.assigned')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resource.details')),
            ],
        ),
    ]
