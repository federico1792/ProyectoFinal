# Generated by Django 4.1.4 on 2023-02-01 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_alter_sale_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='sold',
            field=models.BooleanField(default=False),
        ),
    ]
