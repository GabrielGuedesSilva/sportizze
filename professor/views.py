from django.shortcuts import render

def professor (request):
    return render (
        request,
        'professor/professor.html'
    )
