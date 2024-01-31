from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='base_generic.html'),
    path('course_list/<str:subject>/', views.course_list, name='course_list'),
    path('course_detail/<int:pk>/', views.course_detail, name='course_list'),
    path('module/<int:pk>/<str:module>', views.module_detail, name='module_detail')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
