from django.urls import path
from . import views


app_name = 'invoice'


urlpatterns = [
    path('', views.invoice_list, name='list'),
    path('create/', views.invoice_create, name='create'),
    path('<int:pk>/update/', views.invoice_update, name='update'),
    path('<str:invoice_code>/', views.invoice_detail, name='detail'),
]
