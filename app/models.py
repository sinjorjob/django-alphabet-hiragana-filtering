from django.db import models

class Book(models.Model):
    
   name = models.CharField(verbose_name="書籍名", max_length=255)
   price = models.IntegerField(verbose_name="値段")

   def __str__(self):
       return self.name