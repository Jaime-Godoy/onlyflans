from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView #para que se pueda usar el CRUD
from .models import Flan
from .forms import ContactFormForm, FlanForm
from django.contrib.auth.views import LoginView, LogoutView #para que se pueda usar el login y logout
from django.contrib.auth.decorators import login_required #para que solo los usuarios logueados puedan ver la pagina welcome

# Create your views here.
def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html',{'flanes': flanes_publicos})

def about(request):

    return render(request, 'about.html')

@login_required
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

def flan_detail(request,flan_id):
    flan = get_object_or_404(Flan,pk=flan_id)
    return render(request, 'flan_detail.html', {'flan':flan})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
    next_page = '/'

# creacion de CRUD
class FlanCreateView(CreateView):
    model = Flan
    form_class = FlanForm
    template_name = 'flan_form.html'  # Ajusta según el nombre de tu plantilla
    success_url = reverse_lazy('index')  # Redirecciona a la página principal después de la creación
# class FlanCreateView(CreateView):
#     model = Flan
#     template_name = 'flan_form.html'
#     fields = ['name', 'description', 'is_private']
#     success_url = '/'

class FlanUpdateView(UpdateView):
    model = Flan
    template_name = 'flan_form.html'
    fields = ['name', 'description','price_clp','image_url', 'is_private']
    success_url = '/'

class FlanDeleteView(DeleteView):
    model = Flan
    template_name = 'flan_confirm_delete.html'
    success_url = '/'

def handler404(request):
    return render(request, '404.html', status=404)