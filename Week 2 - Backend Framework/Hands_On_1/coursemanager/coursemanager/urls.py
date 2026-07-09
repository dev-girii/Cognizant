from django.contrib import admin
from django.urls import path, include
from courses.views import hello_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/hello/', hello_view, name='api_hello'),
    path('api/', include('courses.urls')),
]