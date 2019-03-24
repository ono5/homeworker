from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_item= models.CharField(max_length=25, blank=False, null=True)

    def __str__(self):
        return self.category_item


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)
    item = models.CharField(max_length=250, blank=False, null=True)
    credit = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=False,
        null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id', )

    def __str__(self):
        return self.item
