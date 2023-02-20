from django.http import HttpResponse
from django.shortcuts import render
import string


def index(request):
    return render(request, 'index.html')

def analyze(request):
    text_to_analyze = request.POST.get('text', 'default')
    option = request.POST.get('option', 'off')

    analyzed_text = ""

    if option == 'removepunc':
        for char in text_to_analyze:
            if char not in string.punctuation:
                analyzed_text += char

        params = {
            'purpose': 'Removed Punctuation',
            'analyzed_text': analyzed_text
        }
        return render(request, 'analyze.html', params)
    elif option == 'capfirst':
        analyzed_text = text_to_analyze.capitalize()

        params = {
            'purpose': 'Capitalized First',
            'analyzed_text': analyzed_text
        }
        return render(request, 'analyze.html', params)
    elif option == 'capall':
        analyzed_text = text_to_analyze.upper()

        params = {
            'purpose': 'Capitalized All',
            'analyzed_text': analyzed_text
        }
        return render(request, 'analyze.html', params)
    elif option == 'newlineremover':
        for char in text_to_analyze:
            if char != '\n' and char !='\r':
                analyzed_text += char
        params = {
            'purpose': 'Removed New Lines',
            'analyzed_text': analyzed_text
        }
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")