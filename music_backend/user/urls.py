from django.urls import path, include
from .views import RegisterView, LoginView, UserSubsubscriberViewset, ListPremiumUser
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user_subscribe', UserSubsubscriberViewset, basename='user_subscribe')
router.register(r'list_prime_users',ListPremiumUser,basename="list_prime_users")

urlpatterns = [
    path('register/',RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('',include(router.urls)),
]
