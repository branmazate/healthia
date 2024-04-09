import openai
from django.conf import settings

def extract_symptoms(user_input):
    openai.api_key = settings.OPENAI_API_KEY

    # Promt for symptom extraction

    prompt = f"Identify and list potential medical symptoms for the following user input {user_input}."

    # Generación de la respuesta
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.3,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )
    
    #Response processing.
    symptoms = response.choices[0].text.split(',')
    return [symptoms.strip() for symptom in symptoms if symptoms.strip()]
