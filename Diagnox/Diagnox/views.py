from django.shortcuts import redirect, render

def acc(request):
    return render(request, 'index.html')
