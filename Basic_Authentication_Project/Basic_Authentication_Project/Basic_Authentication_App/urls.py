
from django.conf.urls import url,include
from .views import EmpViewSet

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('emp_viewset',EmpViewSet)

urlpatterns = [
    url(r'',include(router.urls))
]