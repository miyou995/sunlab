

from django.contrib import admin
from django.urls import path, include
from config import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("core.urls")),
    path('cart/', include("cart.urls")),
    path('orders/', include("order.urls")),
    path('coupons/', include("coupons.urls")),
    path('delivery/', include("delivery.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),