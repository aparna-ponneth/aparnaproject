# Generated by Django 4.1.5 on 2023-01-12 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admindb',
            old_name='Name',
            new_name='Username',
        ),
        migrations.AddField(
            model_name='admindb',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='admin'),
        ),
    ]