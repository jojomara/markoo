from django.urls import path
from hello import views
from .views import search_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add, name="add"),
    path('addrec/', views.addrec, name="addrec"),
    path('delete/<int:id>/', views.delete, name="delete"),  
    path('update/<int:id>/', views.update, name="update"),
    path('update/uprec/<int:id>/', views.uprec, name="uprec"),  # Assuming uprec is a different view
    path('dropdownsearch/', views.dropdownsearch, name="dropdownsearch"),  #  unique path
    path('search/', search_view, name='search_view'),
    path('image_upload/', views.image_upload),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)