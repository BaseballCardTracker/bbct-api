from django.urls import path, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from api import views

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'baseball_cards', views.BaseballCardViewSet)

schema_view = get_schema_view(
    title="BBCT",
    description="Baseball Card Tracker API",
    version="1.0.0"
)

urlpatterns = [
    path('', include(router.urls)),
    path('docs/', schema_view, name='docs'),
]
