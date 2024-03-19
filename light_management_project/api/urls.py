from django.urls import path
from .views import LightsManage, RoomLightsAPIView

urlpatterns = [
    path('lights-manage/', LightsManage.as_view(), name='lights-manage'),
    path('room-lights/<int:pk>', RoomLightsAPIView.as_view(), name='room-lights'),
]