from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='TaskFusion API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view),
    
    path('authe/', include('authe.urls')),
    path('tasks/', include('tasks.urls')),
    path('taskboards/', include('taskboards.urls')),
]
