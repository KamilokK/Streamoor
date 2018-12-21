from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.conf import settings
from django.contrib.auth.forms import PasswordChangeForm



# Create your views here.


class HomeView(View):
    def get(self, request):
        return render(request, "home.html")


class EndView(View):
    def get(self, request):
        return render(request, "base.html")

class MainView(View):
    def get(self, request):
        return render(request, "base.html")


class AddUserView(View):
    def get(self, request):
        form = AddUserForm()
        return render(request, "streamooruser_form.html", {'form': form})

    def post(self, request):
        form = AddUserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            user = form.cleaned_data.get('user')
            user_stream = form.cleaned_data.get('user_stream')
            email = form.cleaned_data.get('email')
            add_user = User.objects.create_user(username=user, password=password, email=email)
            streamoor_user = StreamoorUser.objects.create(user=add_user, user_stream=user_stream)
            return redirect('/Streamoor')
        return render(request, "streamooruser_form.html", {'form': form})



class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('user'),
                                password=form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                return redirect('/Streamoor')
            else:
                return HttpResponse('Zły login lub hasło!')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/Streamoor')


class DealView(View):

    def get(self, request):
        users = User.objects.all()
        return render(request, "deals.html", {"users": users})

class UserView(DetailView):
   model = User()


class UserProfile(View):

    def get(self, request, pk):
        user = User.objects.get(id= pk)
        return render(request, "user.html", {"name": user.username, "email": user.email,
                                                          "user_stream": user.streamooruser.user_stream})

class StreamoorUserUpdate(UpdateView):

  model = User
  fields = ['username', 'email', 'password']
  template_name = 'stremooruser_update_form.html'
  success_url = '/Streamoor'


class StreamoorUserDelete(DeleteView):

  model = User
  template_name = 'stremooruser_confirm_delete.html'
  success_url = '/Streamoor'



class SearchNetflix(LoginRequiredMixin, View):
    login_url = "/login"

    def get(self, request):
        streamoorusers = StreamoorUser.objects.exclude(user_stream=1)
        return render(request, "search.html", {"streamoorusers": streamoorusers})


class SearchHBO(LoginRequiredMixin, View):
    login_url = "/login"

    def get(self, request):
        streamoorusers = StreamoorUser.objects.exclude(user_stream=2)

        return render(request, "search.html", {"streamoorusers": streamoorusers})



class SearchAmazon(LoginRequiredMixin, View):

    login_url = "/login"
    def get(self, request):
        streamoorusers = StreamoorUser.objects.exclude(user_stream=3)
        return render(request, "search.html", {"streamoorusers": streamoorusers})




