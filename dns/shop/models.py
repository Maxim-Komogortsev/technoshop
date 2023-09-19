from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.
class Category(models.Model):
    slug = models.SlugField(max_length=30, unique=True, db_index=True)
    name = models.CharField(max_length=30, db_index=True)

    class Meta:
        ordering = ("name", )
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('show_product_list_by_category', args=[self.slug])


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=30, db_index=True)
    img = models.ImageField(blank=True, upload_to='products/%Y/%m/%d')
    description = models.TextField(max_length=2000, blank=True, null=True)
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("name", )
        index_together = (('id', 'slug'), )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_info', args=[self.id, self.slug])

    def get_absolute_image_url(self):
        return f'{settings.MEDIA_URL}{self.img}'