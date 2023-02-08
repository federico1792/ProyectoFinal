from django.db import models

class IndexChange(models.Model):
    background = models.ImageField(upload_to='index_image', null=True, blank=True, verbose_name='Imagen Principal')
    team = models.CharField(max_length=50, null=True, blank=True, verbose_name='Titulo de equipo')
    img1 = models.ImageField(upload_to='index_image', null=True, blank=True)
    title1 = models.CharField(max_length=50, null=True, blank=True, verbose_name='Persona 1')
    description1 = models.CharField(max_length=300, null=True, blank=True)
    img2 = models.ImageField(upload_to='index_image', null=True, blank=True)
    title2 = models.CharField(max_length=50, null=True, blank=True, verbose_name='Persona 2')
    description2 = models.CharField(max_length=300, null=True, blank=True)
    img3 = models.ImageField(upload_to='index_image', null=True, blank=True)
    title3 = models.CharField(max_length=50, null=True, blank=True, verbose_name='Persona 3')
    description3 = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.team

    class Meta:
        verbose_name = 'Modificacion'
        verbose_name_plural = 'Modificaciones'