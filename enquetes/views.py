from django.shortcuts import render

def enquetes (request):
    return render (request, "enquetes-index.html")