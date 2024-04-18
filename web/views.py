from django.shortcuts import render, redirect
from .models import Flan
from .forms import ContactFormForm

# Create your views here.
def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html',{'flanes': flanes_publicos})

def about(request):

    return render(request, 'about.html')

def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html',{'flanes': flanes_privados})

def contact(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactFormForm()

    return render(request, 'contact.html', {'form':form} )

def success(request):
    return render(request, 'success.html')
