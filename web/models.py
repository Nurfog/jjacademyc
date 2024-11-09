from django.db import models

class Banner(models.Model):
    idbanner = models.AutoField(primary_key=True,null=False)
    img = models.ImageField(null=False)
    posicion = models.IntegerField(null=False)
    activo = models.BooleanField(default=True,null=False)
    
    class Meta:
        verbose_name = 'banner'
    def __str__(self):
        return self.img
