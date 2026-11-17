from django.urls import path
from .views import CartGetPostView, CartDetailPutPatchDelete

urlpatterns = [
    path('cart/', CartGetPostView.as_view(), name='cart'),
    path('cart/<int:pk>/', CartDetailPutPatchDelete.as_view(), name='cart_detail'),
]