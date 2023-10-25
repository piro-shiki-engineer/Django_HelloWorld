from django.contrib import admin
from django.urls import path, include
from .views import helloworld_function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('HelloWorld/', helloworld_function),
    path('helloapp', include('helloworld_app.urls'))
]
