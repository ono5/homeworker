from django.db import models


class Category(models.Model):
    category_item= models.CharField(max_length=25, blank=False, null=True)

    def __str__(self):
        return self.category


class Payment(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)
    credit = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=False,
        null=True)
    item = models.CharField(max_length=250, blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id', )

    def __str__(self):
        return self.product
