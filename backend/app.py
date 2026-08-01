from chatbot import get_response
def wlc():
        print("==================================")
        print("     Welcome to SpeakMate    ")
        print("Your AI English Speaking Partner")
        print("==================================")
        print("Hello!")
        print("I'm SpeakMate...")
        print("Let's improve your English together..")
wlc()   

def greet():
        while True:            
                print("What's Your name?")
                name=input("Please enter your name: ") 
                name=name.title()#title is use for correcting input sequence like suKANYA to this Sukanya
                name=name.strip()#.strip is use for removing extra space
                if name=="":
                  print("Please enter your name to move forward")
                else:
                       break 
        print(f"Nice to meet you ,{name} !") 
        return name      
name=greet()

print("\n What would you like to talk about today?")
while True:
     user_msg = input("You: ")
     if( user_msg.strip().lower() == "bye"):
        print("Thank you for practicing English with SpeakMate...")
        print("Have a wonderful day!")
        break 
     ai_response=get_response(user_msg)  #function call from chatbot.py
     print(ai_response)