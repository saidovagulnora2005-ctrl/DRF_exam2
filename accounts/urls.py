from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import *

urlpatterns = [
    path('', register_view),
    path('login/', login_view,),
    path('refresh/', refresh_token_view),
    path('logout/', logout_view),
]