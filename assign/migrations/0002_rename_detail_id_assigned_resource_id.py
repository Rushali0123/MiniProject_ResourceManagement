# Generated by Django 4.2.1 on 2023-05-24 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assign', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assigned',
            old_name='detail_id',
            new_name='resource_id',
        ),
    ]
