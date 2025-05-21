from django.shortcuts import render, HttpResponse
from .main import main
# Create your views here.

def home(request):
    return render(request,'home.html')


def chat(request):
    query = request.GET.get('query', '')
    print(f"Received query: {query}")  # Debugging output
    result = main(query)
    return render(request, 'chat.html', {
        'content': result.get("message", ""),
        'open_url': result.get("open_url", "")
    })


