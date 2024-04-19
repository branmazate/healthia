from ..models import UserQuery, ChatResponse
from django.core.exceptions import ValidationError

def process_query(user_query):
    """
    Process the user query to extract symptoms and other relevant information
    """
    try:
        user_query.symptoms
        user_query.save()
    except:
        
        raise