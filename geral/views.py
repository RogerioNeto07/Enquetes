from django.shortcuts import render

def coreindex(request):
    return render (request, "core-index.html")
