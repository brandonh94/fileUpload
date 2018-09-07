from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.FileList.as_view()),
    path('home/', views.index, name='index'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
