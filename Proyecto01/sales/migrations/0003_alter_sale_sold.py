# Generated by Django 4.1.4 on 2023-02-01 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_rename_profile_image_sale_sale_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='sold',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
