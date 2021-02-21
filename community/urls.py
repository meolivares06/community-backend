
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from questions import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'questions', views.QuestionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
