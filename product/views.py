from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Products, Review
from .serializers import (
    CategorySerializer,
    ProductsSerializer,
    ReviewSerializer,
    RatingReviewSerializer,
)


@api_view(["GET", "POST"])
def category_list_api_view(request):
    if request.method == "GET":
        category_list = Category.objects.all()
        category_json = CategorySerializer(instance=category_list, many=True).data
        return Response(data=category_json, status=status.HTTP_200_OK)
    elif request.method == "POST":
        name = request.data.get("name")
        category = Category.objects.create(name=name)
        return Response(CategorySerializer(category).data)


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
        item.name = request.data.get("name")
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
        price = request.data.get("price")
        name_id = request.data.get("name_id")
        product = Products.objects.create(
            title=title, description=description, price=price, name_id=name_id
        )
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
        text = request.data.get("text")
        product_id = request.data.get("product_id")
        stars = request.data.get("stars")
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
        item.text = request.data.get("text")
        item.products_id = request.data.get("products_id")
        item.stars = request.data.get("stars")
        item.save()
        return Response(data=ReviewSerializer(item).data)
