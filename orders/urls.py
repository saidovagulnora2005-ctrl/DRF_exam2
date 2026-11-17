from django.urls import path
from .views import OrderGetPostView, OrderDetailPutPatchDelete

urlpatterns = [
    path('orders/', OrderGetPostView.as_view(), name='orders'),
    path('orders/<int:pk>/', OrderDetailPutPatchDelete.as_view(), name='order_detail'),
]