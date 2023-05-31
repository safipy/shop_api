from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Products(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.BooleanField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField()
    producrs = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


