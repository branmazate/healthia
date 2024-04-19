from .chatbot import generate_chatbot_response
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
from .chatbot import generate_chatbot_response
from .services.symptom_service import process_user_query_and_extract_symptoms

class UserQueryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user queries.
    It handles the CRUD operations automatically and includes
    custom logic for processing user queries upon creation.
    """
    queryset = UserQuery.objects.all().prefetch_related('chatresponse_set')
    serializer_class = UserQuerySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        """
        Processes the creation of UserQuery instances.
        It saves the new query, processes it for symptom extraction,
        and generates a chatbot response.
        """
        serializer.save(user=self.request.user)
        #Save the new userQuery instance
        user_query = serializer.instance
        
        #Process the query for symptom extraction and handling
        process_user_query_and_extract_symptoms(user_query)
        #Generate and store the chatbot response
        chatbot_response_text = generate_chatbot_response(user_query.query_text)
        if chatbot_response_text:
            ChatResponse.objects.create(query=user_query, response_text=chatbot_response_text)
    
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