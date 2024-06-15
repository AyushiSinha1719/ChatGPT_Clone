from django.shortcuts import render
from openai import OpenAI
from django.http import JsonResponse
from .models import Chat


# Create your views here.
client = OpenAI(api_key='YOUR API KEY')

def index(request):
    return render(request, 'index.html')

def response(request):
    if request.method == 'POST':
        message = request.POST.get('message', '') #if not message,leave empty

        completion = client.chat.completions.create( #for response --Create a chat completion request:
            model='gpt-3.5-turbo-16k',
            messages=[ #role (either "system", "user", or "assistant") 
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ]
        )

        answer = completion.choices[0].message.content #The generated response is accessed through completion.choices[0].message['content'].
        new_chat = Chat(message=message, response=answer)
        new_chat.save() #Before sending response,save all the data
        return JsonResponse({'response': answer}) #answer will be in form of JSON
    return JsonResponse({'response': 'Invalid request'}, status=400) #if method is not POST