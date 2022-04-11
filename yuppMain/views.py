from django.shortcuts import redirect, render
from .models import contacts, prodImage, products
# Create your views here.

def home(request):
    prod = products.objects.all()
    prodImageObj = prodImage.objects.all()
    return render(request, 'index.html', context={'prod' : prod, 'prodImageObj' : prodImageObj})

def blog(request):
    prod = products.objects.all()
    return render(request, 'blog/index.html', context={'prod' : prod})

def productss(request):
    prod = products.objects.all()
    prodImageObj = prodImage.objects.all()
    return render(request, 'product/index/index.html', context={'prod' : prod, 'prodImageObj' : prodImageObj})



def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']

        contacts.objects.create(
            name = name, 
            email = email,
            phone = phone,
            subject = subject,
            message = message
        )
        return redirect("/contact/")
    prod = products.objects.all()
    return render(request, 'contact/index.html', context={'prod' : prod})

def about_us(request):
    prod = products.objects.all()
    return render(request, 'about-us/index.html', context={'prod' : prod})

def productImg(request, id):
    prod = products.objects.all()
    productImgObj = prodImage.objects.filter(product = products.objects.get(id=id))
    return render(request, 'product/index/index.html', context={'prod' : prod, 'prodImageObj' : productImgObj})

