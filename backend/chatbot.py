from google import genai # Import Gemini SDK
from config import api_key

client=genai.Client(api_key=api_key)

def get_response(user_message):
    response=client.models.generate_content(
       model="gemini-3-flash-preview",
        contents=user_message
    )

    return response.text
