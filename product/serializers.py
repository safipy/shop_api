from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Category, Products, Review, Tag


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


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required=True)
    products_id = serializers.IntegerField(min_value=1)
    stars = serializers.IntegerField(required=True)


class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)


class TagValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)


class ProductsValidateSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    category_id = serializers.IntegerField(min_value=1)
    tags = serializers.ListField(child=serializers.IntegerField(min_value=1))

    def validate_category_id(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError("Category doesn't exists")
        return category_id

    def validate_tags(self, tags):
        tags_db = Tag.objects.filter(products__category_id__in=tags)
        if len(tags_db) != len(tags):
            tags_db_id = set(tag.id for tag in tags_db)
            diff_values = [tag_id for tag_id in tags if tag_id not in tags_db_id]
            raise ValidationError(f"Tags doesn't exists: {diff_values}")
        return tags
