from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserFilesView.as_view(), name='files'),
    path('<int:pk>/', views.UserFileDetialView.as_view(), name='file-details'),
    path('delete/<int:pk>/', views.UserFileDelete.as_view(), name='delete-file'),
    path('add/', views.upload_file, name='add-file'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
