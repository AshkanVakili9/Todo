from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('todo', TodoViewSet, basename='todo')

urlpatterns = [
    # path('add/', add),
    # path('list/', list),
    # path('update/<int:id>', update),
    # path('delete/<int:id>', delete),

    # path('', TodoAPIView.as_view(), name='api'),

    path('app/', include(router.urls))
]
