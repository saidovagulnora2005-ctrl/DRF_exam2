from django.urls import path
from .views import MedicamentGetPostView, MedicamentDetailPutPatchDelete

urlpatterns = [
    path('medicaments/', MedicamentGetPostView.as_view(), name='medicament_list_create'),
    path('medicaments/<int:pk>/', MedicamentDetailPutPatchDelete.as_view(), name='medicament_detail'),
]