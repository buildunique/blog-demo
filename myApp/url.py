from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from myApp import views

urlpatterns = [
    path('',views.home),
    path('blog/<slug:url>',views.post),
    path('category/<slug:url>',views.category)

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
