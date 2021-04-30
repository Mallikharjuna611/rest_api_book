

from django.conf.urls import url ,include
from ModelViewSet_App import views
# from ModelViewSet_App.views import EmpViewSet

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('emp_viewset',views.EmpViewSet)

urlpatterns = [
    url(r'',include(router.urls))
]






