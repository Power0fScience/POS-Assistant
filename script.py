import os
import google.generativeai as genai
import requests
import time
import socket

global gemini
global user_input
global response
global CRED
global CEND
global CGREEN
global Cred
global CYELLOW

Cred = '\033[31m'
CYELLOW = '\033[33m'
CEND = '\033[0m'
CGREEN = '\033[92m'



# check internet
def check_internet_connection():
    remote_server = "www.google.com"
    port = 80
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    try:
        sock.connect((remote_server, port))
        return True
    except socket.error:
        return False
    finally:
        sock.close()


if check_internet_connection():
    print(CGREEN + "Internet is connected." + CEND)
else:
    print(
        Cred + "Internet is not connected, some features may not work, please make sure you got an access to the internet you little piece of shit  ( ͡⚆ ͜ʖ ͡⚆)╭∩╮" + CEND)

# Hna l API setup (free plan 15 request/min)
api_key = os.getenv("PUT YOUR API KEY HERE")
genai.configure(api_key="PUT YOUR API KEY HERE")

# the generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
}

# Initialize the model (don't touch)
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config
)


# Gemini function
def start_gemini():
    global CEND
    chat_history = []
    chat_session = model.start_chat(history=chat_history)
    try:
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit', "let's stop", 'lets stop']:
                print("Exiting chat.")
                break

            elif user_input.lower() in ['shut down','Shut down', 'turn off the pc']:
                os.system("shutdown /p")

            elif user_input.lower() in ["what's your name", 'what can i call you' ,"what's your name?", 'what can i call you?']:
                grey = '\033[35m'
                print(grey + "P.O.S (Offline) " + CEND, ": My name is PowerOfScience, an AI based assistant, you can call me POS.")

            elif user_input.lower() in ['open history', 'send history', 'latest message', 'latest result']:
                grey = '\033[35m'
                print(grey + "P.O.S (Offline) " + CEND, ": sure thing,")

            # Send a message to the chat session
            else:
                response = chat_session.send_message(user_input)

                # Update the chat history
                chat_history.append({"role": "user", "content": user_input})
                chat_history.append({"role": "assistant", "content": response.text})

                # Print the response text
                print(CYELLOW + "P.O.S :" + CEND
                      , response.text)

    except Exception as e:
        CRED = '\033[94m'
        CEND = '\033[0m'
        print(CRED + f"An error occurred: {e}", ",try reopen the app" + CEND)


if __name__ == "__main__":
    start_gemini()
    check_internet_connection()

time.sleep(5)
