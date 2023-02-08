from django.db import models

class Sale(models.Model):
    title = models.CharField(max_length=50, verbose_name='Titutlo')
    zone = models.CharField(max_length=35, verbose_name='Zona')
    description = models.CharField(max_length=300)
    price = models.FloatField(verbose_name='Precio')
    environments = models.IntegerField(verbose_name='Ambientes')
    toilets = models.IntegerField(verbose_name='Baños')
    area = models.FloatField()
    sold = models.BooleanField(verbose_name='Vendido')
    sale_image = models.ImageField(upload_to='sales_image', null=True, blank=True, verbose_name='Imagen')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'