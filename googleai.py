import google.generativeai as generativeai
generativeai.configure(api_key="AIzaSyCwT-fTnParhqysna-TbLAdr4xdfHFx9sQ")
response=generativeai.GenerativeModel("gemini-2.0-flash-exp").generate_content("你是誰?")
print(response.text)