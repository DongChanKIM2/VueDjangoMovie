from django.urls import path, include
from . import views
from rest_framework_jwt.views import obtain_jwt_token
# from django.conf.urls import url

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup),
    path('api-token-auth/', obtain_jwt_token),
    path('myprofile/', views.my_profile),
]
