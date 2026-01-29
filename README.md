To Run simply run the file.
Download Postman API Tester from anywhere (This is because I did not make UI yet)

View the image I added to this repo and try to replicate everything on Postman (MAKE SURE YOU TYPE IN YOUR LOCALHOST IP WHICH FLASK WILL SHOW)

Add this Body ---> raw :

{
  "system_prompt": "Your system instructions here",
  "model_name": "llama-3.3-70b-versatile",
  "messages": ["Hello", "How are you?"]
}

And send the request
