from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Products, Review
from .serializers import CategorySerializer, ProductsSerializer, ReviewSerializer


@api_view(['GET'])
def category_list_api_view(request):
    category_list = Category.objects.all()
    category_json = CategorySerializer(instance=category_list, many=True).data
    return Response(data=category_json, status=status.HTTP_200_OK)

@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        item = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(data={"error": "name not found"}, status=status.HTTP_404_NOT_FOUND)
    category_json = CategorySerializer(instance=item, many=False).data
    return Response(data=category_json, status=status.HTTP_200_OK)


@api_view(["GET"])
def products_list_api_view(request):
    products_list = Products.objects.all()
    products_json = ProductsSerializer(instance=products_list, many=True).data
    return Response(data=products_json, status=status.HTTP_200_OK)

@api_view(["GET"])
def products_detail_api_view(request, id):
    try:
        item = Products.objects.get(id=id)
    except Products.DoesNotExist:
        return Response(data={"error": "Products not found"}, status=status.HTTP_404_NOT_FOUND)
    products_json = ProductsSerializer(instance=item, many=False).data
    return Response(data=products_json, status=status.HTTP_200_OK)


@api_view(["GET"])
def review_list_api_view(request):
    review_list = Review.objects.all()
    review_json = ReviewSerializer(instance=review_list, many=True).data
    return Response(data=review_json, status=status.HTTP_200_OK)

@api_view(["GET"])
def review_detail_api_view(request, id):
    try:
        item = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={"error": "Review not found"}, status=status.HTTP_404_NOT_FOUND)
    review_json = ReviewSerializer(instance=item, many=False).data
    return Response(data=review_json, status=status.HTTP_200_OK)







