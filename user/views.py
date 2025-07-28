from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from base.response import BadRequest
from user.models import CustomUser
from rest_framework.decorators import action
from user.serializers import DumyUserSerializer, CustomUserSerializer

"""Registraction of a new user"""
class RegisterView(APIView):
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({'message': 'Registration Successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

"""This will return one access and refresh token
Once the user is confirmed"""
class LoginView(APIView):
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if(serializer.is_valid()):
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            return Response({
                'response': "user logged in successfully",
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


# Update subscription plan for user
class UserSubsubscriberViewset(viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = DumyUserSerializer
    
    @action(detail=False, methods=['post'], url_path='update_sub')
    def update_sub(self, request):
        data = request.data
        user_id = data.get('customer_id')
        upgrade_subscription = data.get('is_sub')

        if(user_id is None):
            return BadRequest({"error":"User id cannot be none"})
        
        user = CustomUser.objects.filter(id=user_id).first()
        if(user is None):
            return BadRequest({"error":"Invalid User Id"})
        
        if(upgrade_subscription is None):
            return BadRequest({"error":"Tell something about upgrade_sub"})
        user.is_subscriber = bool(upgrade_subscription)
        user.save()
        return Response({"Message":"Subscription Updated Successfully"})


# List all users with subscription Plan
class ListPremiumUser(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = CustomUserSerializer
    
    def get_queryset(self):
        users = CustomUser.objects.filter(is_subscriber=True)
        return users

        




