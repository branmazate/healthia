import openai
from django.conf import settings

def generate_chatbot_response(prompt):
    try:
        openai.api_key = settings.OPENAI_API_KEY
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error generating chatbot response: {e}")
        return None