from dotenv import load_dotenv 
load_dotenv() #this line load .env file i.e,its call dotenv
import os    #this os module is use for accessing the api_key
api_key=os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-flash-lite-latest"