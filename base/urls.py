from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('experience/', views.experience, name='experience'),
    path('projskills/', views.projskills, name='projskills'),
    path('other/', views.other, name='other')
]
