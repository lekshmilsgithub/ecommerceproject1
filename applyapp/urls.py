from django.contrib import admin
from django.urls import path
from applyapp import views

app_name = 'myapp'

urlpatterns = [

    path('', views.apply, name='apply'),
    path('shop/<int:shop_id>', views.detail, name='detail'),
    path('add/', views.add_product, name='add_product'),
    path('update/<int:id>', views.update, name='update'),

    path('delete/<int:id>', views.delete, name='delete'),
]
