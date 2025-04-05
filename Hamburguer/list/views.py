from django.shortcuts import render

def chamar(request):
    return render(request, 'list/index.html', {})
