from django.urls import path
from management.views import ExampleViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('example', ExampleViewSet, basename='example')


urlpatterns = router.urls
