from django.urls import path, include
from rest_framework import routers

from api import views

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'baseball_cards', views.BaseballCardViewSet)

urlpatterns = [
    path('', include(router.urls))
]
