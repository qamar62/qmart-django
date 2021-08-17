from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug =  models.CharField(max_length=100, unique=True)
    decription = models.CharField(max_length=255)
    cat_image =  models.ImageField(upload_to='photos/categories', blank=True)
    created_on =  models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name =  'category'
        verbose_name_plural = 'catagories' 

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])


    def __str__(self):
        return self.name