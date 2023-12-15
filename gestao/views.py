from django.shortcuts import render

def gestao (request):
    return render(
        request,
        'gestao/gestao.html'
    )
