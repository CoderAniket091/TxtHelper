#I created this file - ANIKET DANDGAVHAN
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
     params = {'name':'Aniket', 'place':'Mars'}
     return render(request, 'index.html', params)

def about(request):
    return render(request, 'about.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def analyze(request):
    # GET THE TEXT FROM TEMPLATE TEXTAREA
    djtext = (request.POST.get('text', 'default'))
    print(djtext)

    # CHECK CHECKBOX IS ON OR OFF
    removepunc = (request.POST.get('removepunc', 'off'))
    fullcaps = (request.POST.get('fullcaps', 'off'))
    newlineremover = (request.POST.get('newlineremover', 'off'))
    extraspaceremover = (request.POST.get('extraspaceremover', 'off'))
    charcount = (request.POST.get('charcount', 'off'))

    if removepunc == 'on':
        punctuations = '''!@#$%^&*()_+-=[]{}|;:"'.>?/,<'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': "Removed Punctuations", 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == 'on':
        analyzed = djtext.upper()
        params = {'purpose': "Capitalized", 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': "Removed New Lines", 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': "Removed spaces", 'analyzed_text': analyzed}
        djtext = analyzed

    if charcount == 'on':
        charcount = 0
        for char in djtext:
            if char != " ":
                charcount = charcount + 1
        params2 = {'analyzed_text': analyzed,'analyzed_texts': f"Character count is {charcount}"}
        return render(request, 'analyze.html', params2)

    if (removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and charcount != 'on'):
        return HttpResponse("ERROR404")
    
    return render(request, 'analyze.html', params)
