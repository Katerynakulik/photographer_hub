from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

handler404 = 'home.views.handle_404'
handler500 = 'home.views.handle_500'

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("home.urls")),
    path("photos/", include("products.urls")),
    path("cart/", include("cart.urls")),
    
    # path("checkout/", include("checkout.urls")),
    path("profile/", include("profiles.urls")),
    path("bookings/", include("bookings.urls")),
    path("marketing/", include("marketing.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)