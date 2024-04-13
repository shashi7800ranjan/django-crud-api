from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_data),
    path('add/',views.add_item),
    path('update/<int:pk>/',views.update_item),
    path('delete/<int:pk>/',views.delete_item),
]