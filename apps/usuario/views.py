from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from apps.usuario.forms import LoginForm, AddUser


def index(request):
    return render(request, 'usuario/index.html')


class Login(LoginView):
    form_class = LoginForm
    template_name = 'usuario/login.html'
    success_url = reverse_lazy('home:index')

    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.success_url)


def index(request):
    usuario = User.objects.all()
    return render(request, 'usuario/index.html', {'object_list': usuario})


class ShowUser(ListView):
    model = User
    template_name = 'usuario/table.html'


class RegisterUser(CreateView):
    model = User
    form_class = AddUser
    template_name = 'usuario/add_usuario.html'
    success_url = reverse_lazy('usuario:login')


class UpdateUser(UpdateView):
    model = User
    form_class = User
    template_name = 'usuario/add_usuario.html'
    success_url = reverse_lazy('usuario:index')


class DeleteUser(DeleteView):
    model = User
    template_name = 'usuario/delete_user.html'
    success_url = reverse_lazy('usuario:index')