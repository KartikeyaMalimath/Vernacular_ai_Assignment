from django.db import models

# Create your models here.
class VEntity(models.Model):
    vename = models.TextField(verbose_name='Entity Name')
    vevalue = models.TextField(verbose_name='Entity Value')

    def __str__(self):
        return self.vename
    
    class Meta:
        db_table = 'Entity'