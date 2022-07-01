from django.urls import include, path
from .views import RegisterAPI
# from rest_framework.authtoken import views


urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('register/', RegisterAPI.as_view(), name='register'),
    # path('api-token-auth/', views.obtain_auth_token)
    
]

