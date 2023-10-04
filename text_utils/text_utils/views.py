# I created this file -- Harshit

from django.http import HttpResponse
from django.shortcuts import render # import it show templates

def index(request):
    # params = {'name':'harshit','place':'India'}
    # return render(request,"index.html",params)   #render(request, template, dictionary to use in template)
    return render(request,"index.html")
    # return HttpResponse("Home")

# def about(request):
#     return HttpResponse("about Harshit")

def analyse(request):
    # print(request.GET.get('text','defaut'))# taking the data when it is entered in '/'
    #get the text
    djtext = request.POST.get('text','defaultvalue')

    #checkcheckboxes value
    removepunc = request.POST.get('removepunc','off') #"defaultvalue" on off and "on" value when ticked
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    spaceremover = request.POST.get('spaceremover','off')
    charactercount = request.POST.get('charactercount','off')
    # print(removepunc)
    # print(djtext)

    #check which check box is checked       
    if removepunc == "on":
        analysed = ''
        punctuations = """!()-[];:'"\,<>.?@#$%^&*_~"""
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char
        
        params = {"purpose":"remove punctuations", "analysed_text":analysed}
        djtext = analysed
        # return render(request, "analyse.html",params)
    
    if fullcaps == "on":
        analysed = ""
        for char in djtext:
            analysed = analysed + char.upper()
        params = {"purpose":"Changed to uppercase", "analysed_text":analysed}
        djtext = analysed
        # return render(request, "analyse.html",params)
    
    if newlineremover == "on":
        analysed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analysed = analysed + char
        params = {"purpose":"New line removed", "analysed_text":analysed}
        djtext = analysed
        # return render(request, "analyse.html",params)
    
    if spaceremover == "on":
        analysed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]== " "):
                analysed = analysed + char
        params = {"purpose":"New line removed", "analysed_text":analysed}
        djtext = analysed
        # return render(request, "analyse.html",params)
    
    if charactercount == "on":
        analysed = 0
        for index in range (len(djtext)):
                analysed = analysed + 1
        params = {"purpose":"New line removed", "analysed_text":str(analysed)}
        djtext = analysed
        # return render(request, "analyse.html",params)
     
    # else:
    #     return HttpResponse("error")
    if (fullcaps != "on" and newlineremover != "on" and removepunc != "on" and spaceremover != "on" and charactercount != "on"):
        return HttpResponse("Error") 
    return render(request, "analyse.html",params)
# def capitalizefirst(request):
#     return HttpResponse("capitalizefirst<a href = '/'>home</a>")

# def newlineremove(request):
#     return HttpResponse("newlineremove<a href = '/'>home</a>")

# def spaceremover(request):
#     return HttpResponse("space remover<a href = '/'>home</a>")

# def charcount(request):
#     return HttpResponse("charcounter<a href = '/'>home</a>")