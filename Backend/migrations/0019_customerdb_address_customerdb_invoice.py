# Generated by Django 4.1.5 on 2023-02-20 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0018_roomdb_image2_roomdb_image3'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerdb',
            name='Address',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='customerdb',
            name='Invoice',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]