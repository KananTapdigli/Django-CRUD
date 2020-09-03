from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import *
from .forms import *
from .models import User

class UserListView(ListView):
    model = User
    queryset = User.objects.all()
    template_name = 'home/index.html'

class UserCreateView(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('home')
    template_name = 'user_create/index.html'

class UserEditView(UpdateView):
    model = User
    form_class = UserEditForm
    success_url = reverse_lazy('home')
    template_name = 'user_edit/index.html'
    pk_url_kwarg = 'id'

class UserDetailsView(DetailView):
    model = User
    template_name = 'user_details/index.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'

def delete(request,id):
    activeUser = get_object_or_404(User, id=id)
    activeUser.delete()

    return redirect('home')