from django.urls import path
from .views import helloworldapp_view

urlpatterns = [
    path('helloappworld_app/', helloworldapp_view)
]
