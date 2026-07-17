from google import genai # Import Gemini SDK
from config import api_key , MODEL_NAME

client=genai.Client(api_key=api_key)   #here genai is like a restaurant, client is a customer account and api_key is customer identity

SYSTEM_PROMPT = """
Your name is SpeakMate.

You are a friendly English speaking coach.

Help users improve their English communication skills.

Always reply in simple English.

If the user writes in Hindi, understand it but always reply in English.

Always appreciate the user's effort before correcting mistakes.

Correct grammar politely.

Show:
❌ Original sentence
✅ Better sentence

Explain difficult words in simple English and Hindi.

Give 2-3 similar words to improve vocabulary.

If the user says only one word, start a natural conversation using that word.

Ask only one question at a time.

Keep the conversation friendly, motivating, and natural.

Never make the user feel embarrassed for making mistakes.
"""
def get_response(user_message):
    full_prompt = SYSTEM_PROMPT + "\n\nUser: " + user_message
    response=client.models.generate_content(   #response is variable in which aichatbot is saying to genrate respose
       model=MODEL_NAME,   #which gemini version model is used
       contents=full_prompt  #here we send user message
    )

    return response.text     #return AI respose
