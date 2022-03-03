from django.urls import path
from . import views

urlpatterns = [
    path('rotmg/collection/', views.MomentCreate.as_view(), name='MomentCreate'),
    path('rotmg/collection/<int:pk>', views.MomentList.as_view(), name='MomentList'),
    path('rotmg/photo/', views.PhotoCreate.as_view(), name='PhotoCreate'),
    path('rotmg/photo/<int:pk>', views.PhotoList.as_view(), name='PhotoList'), 
    # path('rotmg/collection/<int:pk>', views.MomentDetail, name='MomentDetail'),
    # path('rotmg/collection/update/<int:pk>', views.MomentUpdate, name='MomentUpdate'), 
    # path('rotmg/collection/delete/<int:pk>', views.MomentDelete, name='MomentDelete'), 
    # path('rotmg/photo/update/<int:pk>', views.PhotoUpdate, name='PhotoUpdate'), 
    # path('rotmg/photo/delete/<int:pk>', views.PhotoDelete, name='PhotoDelete'), 
]