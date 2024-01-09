from django.shortcuts import render


def accept(request):
    return render(request, 'pdf/accept.html')
