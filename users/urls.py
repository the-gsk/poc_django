# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserDetailsViewSet

router = DefaultRouter()
router.register(r'user-details', UserDetailsViewSet, basename='user-details')

urlpatterns = [
    path('api/', include(router.urls)),
]
