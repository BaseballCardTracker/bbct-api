from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from api import views

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'baseball_cards', views.BaseballCardViewSet)
router.register(r'collections', views.CollectionViewSet, 'collection')

schema_view = get_schema_view(
    title="BBCT",
    description="Baseball Card Tracker API",
    version="1.0.0"
)

urlpatterns = [
    path('', include(router.urls)),
    path('openapi-schema/', schema_view, name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'api:openapi-schema'}
    ), name='swagger-ui'),
]
