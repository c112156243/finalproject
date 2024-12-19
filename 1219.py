
import os
import google.generativeai as ai

ai.configure(api_key="AIzaSyBdAlMMlaNrW3YLlDND6pftAzRARSN6x6Y")
response = ai.GenerativeModel('gemini-2.0-flash-exp').generate_content('Who are you')
print(response.text)