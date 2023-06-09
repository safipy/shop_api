from django.conf.urls.static import static
from month_5 import settings
from django.urls import path, include

urlpatterns = [

    path('api/v1/', include('product.urls')),
    path('api/v1/users/', include('users.urls'))

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)