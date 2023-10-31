from django.shortcuts import render
from g4f import ChatCompletion
from django.http import JsonResponse

def chat_view(request):
    request.endpoint = 'GPT'
    return render(request, 'gpt/chat.html')

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def ans(request, models, answer):
    if is_ajax(request=request):
        completion = ChatCompletion.create(
            model=models,
            messages=[{"role": "user", "content": answer}],
        )
        data = {
            'question': answer,
            'answer': completion
        }
        return JsonResponse(data)