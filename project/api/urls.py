from django.urls import path

from .views import (
    LoginView, LogoutView, RegisterView
)

urlpatterns = [
    path('login/', LoginView.as_view(), name='api-login'),
    path('logout/', LogoutView.as_view(), name='api-logout'),
    path('register/', RegisterView.as_view(), name='api-register')
]
from project.token_auth.views import ObtainTokenLoginView
from .views import ProductsView

urlpatterns = [
    path('login/', ObtainTokenLoginView.as_view(), name='api-login'),
    path('products/', ProductsView.as_view(), name='products'),
]
