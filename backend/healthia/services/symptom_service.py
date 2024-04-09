from .openai_service import extract_symptoms
from ..models import DetectedSymptom

def process_user_query_and_extract_symptoms(user_query):
    #Extract symptoms from the query text using OpenAI
    extracted_symptoms = extract_symptoms(user_query.query_text)
    
    #TODO add mapping to standardized symptoms.
    
    #Storing
    for symptom_text in extracted_symptoms:
        DetectedSymptom.objects.create(
            user=user_query.user, 
            symptom_text=symptom_text)