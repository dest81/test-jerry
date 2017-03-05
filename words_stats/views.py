from django.shortcuts import render
from utils import Word


def home(request):
    context = {}
    if request.method == "POST":
        text = request.POST['text']
        context['results'] = Word(text).result()
        context['text'] = text

    return render(request, 'home.html', context)
