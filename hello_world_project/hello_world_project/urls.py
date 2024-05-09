from django.contrib import admin
from django.urls import path
from hello_world_app.views import HelloWorldView

urlpatterns = [
    path('hello/', HelloWorldView.as_view(), name='hello_world'),
    path('admin/', admin.site.urls),
]
