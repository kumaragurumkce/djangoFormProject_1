from django.shortcuts import render
from .models import TextContent,Home_card
from .form import ImageHomeForm
 
# Create your views here.
def form_submit(request):
    return render(request,"htmlfiles/form_submit.html")

def home_page(request):
    title1="Home Pages1"
    print(title1,"........")
    
    title_page=TextContent.objects.first()
    card_content=Home_card.objects.all()
    



    title1=title_page.title if title_page else "title"
    print(title_page,"........")
    print(title1,"........")
    return render(request,"htmlfiles/home.html",{'title1':title1,'home_card':card_content})
   

def upload_page(request):
    print("Reached upload_page view")
    if request.method == 'POST':
        form11 = ImageHomeForm(request.POST, request.FILES)
        print(form11)
        
        if form11.is_valid():
            form11.save()
            return redirect('home_page')
    else:
        form11 = ImageHomeForm()
        print(form11)
        print("Form initialized for GET request")
    return render(request, "htmlfiles/upload_page.html", {'form11': form11})


def collections_page(request):

    return render(request,"htmlfiles/collections.html")


def trends_page(request):
    return render(request,"htmlfiles/trends.html")


def traditional_page(request):
    return render(request,"htmlfiles/traditional.html")


def contact_page(request):
    return render(request,"htmlfiles/contact.html")


def about_page(request):
    return render(request,"htmlfiles/about.html")

def cartList_page(request):
    return render(request,"htmlfiles/cartList.html")

def upload_page(request):
    return render(request,"htmlfiles/upload_page.html")