from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to="static_files/images/category")
    slug = models.CharField(max_length=50)
    parent_id = models.ForeignKey('Category', models.CASCADE, 'category_to_category_pk', blank=True, null=True)


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = RichTextField()
    image = models.ImageField(upload_to="static_files/images/product")
    slug = models.CharField(max_length=50)
    category_id = models.ForeignKey('Category', models.CASCADE, 'category_to_product')
    old_price = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Slider(models.Model):
    top_title = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    buttom_title = models.CharField(max_length=150)
    buttom_html = models.TextField()
    clas = models.CharField(max_length=150)
    sort = models.IntegerField()