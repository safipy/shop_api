from rest_framework import serializers
from .models import Category, Products, Review


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "id name products_count".split()


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class RatingReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Products
        fields = "title rating reviews".split()
