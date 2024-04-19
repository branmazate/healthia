import openai
from django.conf import settings

def extract_symptoms(user_input):
    openai.api_key = settings.OPENAI_API_KEY
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role":"system","content":"You are a greatfull assistant."},
                {"role":"user","content":f"{user_input}"}
                ]
        )
        return response['choices'][0]['message']['content'].strip().split(',')
    except Exception as e:
        print(f"Error generating chatbot response: {e}")
        return []