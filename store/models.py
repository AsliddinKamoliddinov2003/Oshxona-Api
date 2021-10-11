from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager as BaseUserManager



class Category(models.Model):
    class Meta:
        verbose_name="Category"
        verbose_name_plural="Categories"

    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    name = models.CharField(max_length=255)
    price = models.IntegerField(default=False)
    rating = models.FloatField()
    slug = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to = "images/", null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


