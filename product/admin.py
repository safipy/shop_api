from django.contrib import admin
from .models import Category, Products, Review, Tag

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Review)
admin.site.register(Tag)
