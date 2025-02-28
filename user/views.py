from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser,IsAuthenticated

# Create login system 
# or Create a new user
# Display existing users(But read only and admin only)





