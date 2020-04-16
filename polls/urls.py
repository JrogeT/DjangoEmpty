from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='HOME'),
    path('test', views.test, name='TEST'),
    path('page', views.page, name='PAGE'),
]