#Rest_framework packages.
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
#App constructed packages
from .serializers import UserSerializer, UserQuerySerializer, ChatResponseSerializer
from .models import UserQuery, ChatResponse

class UserQueryViewSet(viewsets.ModelViewSet):
    queryset = UserQuery.objects.all()
    serializer_class = UserQuerySerializer
    permission_classes = [IsAuthenticated]
    
class ChatResponseViewSet(viewsets.ModelViewSet):
    queryset = ChatResponse.objects.all()
    serializer_class = ChatResponseSerializer

#User registration view
class UserCreate(APIView):
    # Allow any user to access this url
    permission_classes = ()
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#User logout view
class Logout(APIView):
    authentication_classes = (TokenAuthentication)
    
    def post(self,request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)