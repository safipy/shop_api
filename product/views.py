from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Products, Review, Tag
from .serializers import (
    CategorySerializer,
    CategoryValidateSerializer,
    ProductsSerializer,
    ProductsValidateSerializer,
    ReviewSerializer,
    ReviewValidateSerializer,
    RatingReviewSerializer,
    TagSerializer,
    TagValidateSerializer,
)


@api_view(["GET", "POST"])
def tag_list_api_view(request):
    if request.method == "GET":
        tag_list = Tag.objects.all()
        tag_json = TagSerializer(instance=tag_list, many=True).data
        return Response(data=tag_json)
    elif request.method == "POST":
        serializer = TagValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data.get("name")
        tag = Tag.objects.create(name=name)
        return Response(data=TagSerializer(tag).data)


@api_view(["GET", "DELETE", "PUT"])
def tag_detail_api_view(request, id):
    try:
        item = Tag.objects.get(id=id)
    except Tag.DoesNotExist:
        return Response(
            data={"error": "Tag not found"}, status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":
        tag_json = TagSerializer(instance=item, many=False).data
        return Response(data=tag_json)
    elif request.method == "DELETE":
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        serializer = TagValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        item.name = serializer.is_valid.get("name")
        item.save()
        return Response(data=TagSerializer(item).data)


@api_view(["GET", "POST"])
def category_list_api_view(request):
    if request.method == "GET":
        category_list = Category.objects.all()
        category_json = CategorySerializer(instance=category_list, many=True).data
        return Response(data=category_json, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = CategoryValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.is_valid.get("name")
        category = Category.objects.create(name=name)
        return Response(data=CategorySerializer(category).data)


@api_view(["GET", "DELETE", "PUT"])
def category_detail_api_view(request, id):
    try:
        item = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(
            data={"error": "name not found"}, status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":
        category_json = CategorySerializer(instance=item, many=False).data
        return Response(data=category_json)
    elif request.method == "DELETE":
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        serializer = CategoryValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        item.name = serializer.is_valid.get("name")
        item.save()
        return Response(data=CategorySerializer(item).data)


@api_view(["GET", "POST"])
def products_list_api_view(request):
    if request.method == "GET":
        products_list = Products.objects.all()
        products_json = ProductsSerializer(instance=products_list, many=True).data
        return Response(data=products_json, status=status.HTTP_200_OK)
    elif request.method == "POST":
        title = request.data.get("title")
        description = request.data.get("description")

        serializer = ProductsValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        title = serializer.validated_data.get("name")
        description = serializer.validated_data.get("description")
        price = serializer.validated_data.get("price")
        name_id = serializer.validated_data.get("name_id")
        tags = serializer.validated_data.get("tags")
        product = Products.objects.create(
            title=title, description=description, price=price, name_id=name_id
        )
        product.tags.set(tags)
        return Response(data=ProductsSerializer(product).data)


@api_view(["GET"])
def products_review_list_api_view(request):
    products_review_list = Products.objects.all()
    products_review_json = RatingReviewSerializer(
        instance=products_review_list, many=True
    ).data
    return Response(data=products_review_json, status=status.HTTP_200_OK)


@api_view(["GET", "DELETE", "PUT"])
def products_detail_api_view(reqauest, id):
    try:
        item = Products.objects.get(id=id)
    except Products.DoesNotExist:
        return Response(
            data={"error": "Products not found"}, status=status.HTTP_404_NOT_FOUND
        )
    if reqauest.method == "GET":
        products_json = ProductsSerializer(instance=item, many=False).data
        return Response(data=products_json)
    elif reqauest.method == "DELETE":
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif reqauest.method == "PUT":
        item.title = reqauest.data.get("title")
        item.description = reqauest.data.get("description")
        item.price = reqauest.data.get("price")
        item.name_id = reqauest.data.get("name_id")
        item.save()
        return Response(data=ProductsSerializer(item).data)


@api_view(["GET", "POST"])
def review_list_api_view(request):
    if request.method == "GET":
        review_list = Review.objects.all()
        review_json = ReviewSerializer(instance=review_list, many=True).data
        return Response(data=review_json, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = serializer.is_valid.get("text")
        product_id = serializer.is_valid.get("product_id")
        stars = serializer.is_valid.get("stars")
        review = Review.objects.create(
            text=text,
            product_id=product_id,
            stars=stars,
        )
        return Response(data=ReviewSerializer(review).data)


@api_view(["GET", "DELETE", "PUT"])
def review_detail_api_view(request, id):
    try:
        item = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(
            data={"error": "Review not found"}, status=status.HTTP_404_NOT_FOUND
        )
    if request.method == "GET":
        review_json = ReviewSerializer(instance=item, many=False).data
        return Response(data=review_json)
    elif request.method == "DELETE":
        item.delete()
        return Response(data=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        item.text = serializer.is_valid.get("text")
        item.products_id = serializer.is_valid.get("products_id")
        item.stars = serializer.is_valid.get("stars")
        item.save()
        return Response(data=ReviewSerializer(item).data)
