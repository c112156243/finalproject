import os
import google.generativeai as generativeai

generativeai.configure(api_key="AIzaSyA_K_IZ6uqh544j26PzcVSK-E0Av2ev-A0")
response=generativeai.GenerativeModel("gemini-2.0-flash-exp").generate_content("你是誰")
print(response.text)