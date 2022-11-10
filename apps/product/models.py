from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Категория', max_length=50)
    
    class Meta:
        db_table = 'category'
        managed = True
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        

class Product(models.Model):
    pass