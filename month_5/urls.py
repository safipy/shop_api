from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from month_5 import settings
from product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/category/', views.category_list_api_view),
    path('api/v1/category/<int:id>/', views.category_detail_api_view),
    path('api/v1/products/', views.products_list_api_view),
    path('api/v1/products/<int:id>/', views.products_detail_api_view),
    path('api/v1/review/', views.review_list_api_view),
    path('api/v1/review/<int:id>/', views.review_detail_api_view),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)