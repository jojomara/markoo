"""
URL configuration for world project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.urls import path
from hello import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('hello.urls')),
    path('', views.index, name="index"),
    path('add/', views.add, name="add"),
    path('addrec/', views.addrec, name="addrec"),
    path('delete/<int:id>/', views.delete, name="delete"),  
    path('update/<int:id>/', views.update, name="update"),
    path('update/uprec/<int:id>/', views.uprec, name="uprec"),  # Assuming uprec is a different view
    path('dropdownsearch/', views.dropdownsearch, name="dropdownsearch"),  #  unique path

    path('image_upload/', views.image_upload),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)