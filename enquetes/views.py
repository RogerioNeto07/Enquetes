from django.shortcuts import render

def enquetes (request):
    return render (request, "enquetes-index.html")

def coreindex(request):
    return render (request, "core-index.html")