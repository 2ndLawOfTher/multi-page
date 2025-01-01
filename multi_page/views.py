from django.shortcuts import render

def home(request):
    return render(request, 'MyFirstWebsite.html')

def Images(request):
    return render(request, 'Images.html')

def BoldAndItalic(request):
    return render(request, 'bold and italic.html')

def Lists(request):
    return render(request, 'lists.html')

def Tables(request):
    return render(request, 'Tables.html')

def OnMouseOver(request):
    return render(request, 'OnMouseOver.html')