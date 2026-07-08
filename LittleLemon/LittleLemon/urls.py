from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Restaurant import views

router = DefaultRouter()
router.register(r"tables", views.BookingViewSet, basename="booking")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("restaurant/", include("Restaurant.urls")),
    path("api/", include("LittleLemonAPI.urls")),
    path("restaurant/booking/", include(router.urls)),
    #? Djoser authentication
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]