from django.shortcuts import render,redirect
from .models import Member
from django.core.files.storage import FileSystemStorage
from .forms import Member
from hello import *

# Create your views here.

def index(request):
    mem=Member.objects.all()
   
    return render(request, 'index.html', {'members': mem})  # passing a variable to the template for dyn content

def add(request):
    return render(request, 'add.html')
def addrec(request):
    if request.method == 'POST':
        x = request.POST.get('first')
        y = request.POST.get('last')
        z = request.POST.get('country')
        mem = Member(firstname=x, lastname=y, country=z)
        
        # Handle file upload
        photo = request.FILES.get('photo')
        if photo:
            mem.photo = photo
        else:
            mem.photo = None  # Optional: Clear the photo field if no file is uploaded
        
        mem.save()
        return redirect('index')  # Redirect to the index view after saving
    else:
        return redirect('add')  # Redirect to the add page if not a POST request


def delete(request, id):
    mem=Member.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request, id):
    mem=Member.objects.get(id=id)
    return render(request, 'update.html', {'mem': mem})

def uprec(request, id):
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['country']
    mem=Member.objects.get(id=id)
    mem.firstname=x
    mem.lastname=y
    mem.country=z
    mem.save()
    return redirect("/")

def dropdownsearch(request):
    if request.method == 'POST':
        country = request.POST.get('country')
        firstname = request.POST.get('firstname')  # Retrieve 'firstname' from POST data
        mem = Member.objects.filter(country=country, name=firstname)  # Filter by both country and firstname
        return render(request, 'index.html', {'members': mem})
    else:
        displaymem = Member.objects.all()  # Display all members if it's not a POST request
        return render(request, 'index.html', {'members': displaymem})

from django.shortcuts import render
from .models import Member  # Update with your model name

def search_view(request):
    selected_country = request.GET.get('country')
    if selected_country:
        members = Member.objects.filter(country=selected_country)  # Update with your filtering logic
    else:
        members = Member.objects.all()
    
    context = {
        'members': members,
        'countries': ['Uganda', 'Congo', 'USA', 'Ghana'],  # Example country list
    }
    return render(request, 'your_template.html', context)

def image_upload(request):
    if request.method== 'POST':
        my_image = request.FILES['image']
        fs = FileSystemStorage()
        filename = 'hello/static/images'+ my_image.name
        fs.save('hello/static/images, my_image')
    return render(request, 'add.html')