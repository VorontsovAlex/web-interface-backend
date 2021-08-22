from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from refs.models import Language
from users.models import User
from categories.models import Category


class DataFormat(models.Model):
    """Data formats datasets available on"""

    extension = models.CharField(max_length=10)
    description = models.TextField()


class DeliveryMethod(models.Model):
    """Method represents the way DataSets are may be sent from selller to buyer"""

    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)


class Product(models.Model):
    """Dataset"""

    name = models.CharField(max_length=255, verbose_name='Name of DataSet')
    description = models.TextField()
    category = models.ManyToManyField(Category, verbose_name='Category of dataset', related_name='product_categories')
    languages = models.ManyToManyField(
        Language, blank=True, related_name='product_languages', verbose_name='Languages used'
    )
    data_formats = models.ManyToManyField(DataFormat, blank=True, related_name='product_data_formats')
    delivery_methods = models.ManyToManyField(
        DeliveryMethod, blank=True, related_name='product_delivery_methods',
        verbose_name='Method can be used to deliver dataset to Buyer'
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created', db_index=True)
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated', db_index=True)

    class Meta:
        pass

    def __str__(self):
        return f'{self.name}'


class Review(models.Model):
    """Reviews are given by Buyer"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_reviews')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_reviews')
    message = models.TextField()

    def __str__(self):
        return f'{self.product} - {self.user.name}'


class Sample(models.Model):
    """Sample of Dataset"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_samples')
    path = models.CharField(max_length=255, verbose_name='Path to Dataset sample')

    def __str__(self):
        return self.product.name


class Rate(models.Model):
    """Dataset user rates"""

    value = models.SmallIntegerField(
        verbose_name='User rate presented as integer from 0 to 10',
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_rates')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_rates')
