import os 
import google.generativeai as generativeai

generativeai.configure(api_key="AIzaSyBqigPdLz7JUcm1oA4OGlyqIb1yL5HEcgY")
response = generativeai.GenerativeModel('gemini-2.0-flash-exp').generate_content("你是誰?")
print(response.text)