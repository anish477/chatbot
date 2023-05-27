from django.shortcuts import render
from django.http import JsonResponse
import openai

openai_api_key = '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'
openai.api_key = openai_api_key
def ask_openai(message):
    response=openai.Completion.create(
        model="1"
    )


# Create your views here.
def chatbot(request):
    

    if request.method == 'POST':
        message = request.POST.get('message')
        response = 'hi hhh'
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')
     