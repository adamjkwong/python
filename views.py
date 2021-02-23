from django.shortcuts import render, HttpResponse
from time import gmtime, strftime

#def index(request):
#    return HttpResponse("This is my response!")

def index(request):
    context = {
        "time": strftime("%b %d, %Y", gmtime()),
        "time2": strftime("%X", gmtime())
    }
    return render(request,'index.html', context)

    #%Y-%m-%d %H:%M %p", 