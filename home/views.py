from django.shortcuts import render,HttpResponse

def index(request):
    context={
        'varible':"this is the text"
    }
    return render(request,'index.html',context)
    #return HttpResponse("this home page")

def about(request):
    return HttpResponse("this is about page")
# Create your views here.
def contact(request):
    return HttpResponse("my contact is 7887498918")

def services(request):
    return HttpResponse("i give software services")

