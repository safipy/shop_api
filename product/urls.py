from django.contrib import admin
from django.urls import path
from product import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("category/", views.category_list_api_view),
    path("category/<int:id>/", views.category_detail_api_view),
    path("products/", views.products_list_api_view),
    path("products/<int:id>/", views.products_detail_api_view),
    path("review/", views.review_list_api_view),
    path("review/<int:id>/", views.review_detail_api_view),
    path("products/review/", views.products_review_list_api_view),
    path("tags/", views.tag_list_api_view),
    path("tags/<int:id>/", views.tag_detail_api_view),
]
