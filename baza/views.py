
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


# Create your views here.

class MainView(View):
    def get(self, request):
        return render(request, "base.html")



class StreamoorUserCreate(CreateView):
  model = StreamoorUser
  fields = ['name', 'email', 'user_stream', 'password']
  template_name = 'streamooruser_form.html'
  success_url = reverse_lazy("main")

  def form_valid(self, form):
      user = form.save(commit = False)
      User.objects.create_user(name=user.name, password=user.password)
      return super().form_valid(form)


class StreamoorUserUpdate(UpdateView):

  model = StreamoorUser
  fields = ['name', 'email', 'user_stream', 'password']
  template_name = 'stremooruser_update_form.html'
  success_url = reverse_lazy("main")

class StreamoorUserDelete(DeleteView):

  model = StreamoorUser
  template_name = 'stremooruser_confirm_delete.html'
  success_url = reverse_lazy("main")


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(name=form.cleaned_data.get('login'),
                                password=form.cleaned_data.get('hasło'))
            if user is not None:
                login(request, user)
                return redirect('/Streamoor')
            else:
                return HttpResponse('Zły login lub hasło!')