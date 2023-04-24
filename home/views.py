from django.shortcuts import render, HttpResponse
from home.models import Home , Contact 

# Create your views here.
# def home(request):
#     return render(request,'home.html')

def blog(request):
    return render (request,'blog.html')

# def contact(request):
#     return render(request,'contact.html')

def home(request):
    if request.method=='Post':
        firstname=request.POST.get('firstname')
        emailid=request.POST.get('emailid')
        Home=Home(firstname=firstname,emailid=emailid)
        Home.save()
    return render(request,'home.html')
    
def contact(request):
    if request.method=='Post':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        emailid=request.POST.get('emailid')
        password=request.POST.get('password')
        mobileno=request.POST.get('mobileno')
        address=request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get("state")
        pincode=request.POST.get('pincode')
        Contact=Contact(firstname=firstname, lastname=lastname, emailid=emailid, password=password, mobileno=mobileno, address=address, city=city, state=state, pincode=pincode)
        Contact.save()
    return render(request,'contact.html')
    