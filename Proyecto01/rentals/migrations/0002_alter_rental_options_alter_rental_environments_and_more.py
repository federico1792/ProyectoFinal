# Generated by Django 4.1.4 on 2023-02-08 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rental',
            options={'verbose_name': 'Alquiler', 'verbose_name_plural': 'Alquileres'},
        ),
        migrations.AlterField(
            model_name='rental',
            name='environments',
            field=models.IntegerField(verbose_name='Ambientes'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='price',
            field=models.FloatField(verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='rental_image',
            field=models.ImageField(blank=True, null=True, upload_to='rentals_image', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='sold',
            field=models.BooleanField(verbose_name='Vendido'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='toilets',
            field=models.IntegerField(verbose_name='Baños'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='zone',
            field=models.CharField(max_length=35, verbose_name='Zona'),
        ),
    ]
