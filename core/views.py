from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request,"core/home.html")


def about(request):
    return render(request,"core/about.html")

#def portafolio(request):
#    return render(request,"core/portafolio.html")

def contact(request):
    return render(request,"core/contact.html")

#def contact(request):
#    contact = menu + "<H1>Contact</H1>"
#    return HttpResponse(contact)  