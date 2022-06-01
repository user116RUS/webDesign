from . import views
from django.urls import path

urlpatterns = [
    path('', views.main),
    path('grid/sec/', views.sec),
    path('grids/th/', views.th),
    path('grids/four/', views.four),
    path('grids/', views.grid),
    path('reg/', views.reg),
    path('ank/', views.ank),
    path('order_form/', views.getOrderForm),
    path('video/', views.getVideo),
    path('1/', views.get_book1),
    path('2/', views.get_book2),
    path('3/', views.get_book3),
    path('4/', views.get_book4),


]
