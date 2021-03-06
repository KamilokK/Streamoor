"""StreamDeal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from baza.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^AddUser$', AddUserView.as_view(), name="dodaj"),
    url(r'^Streamoor$', MainView.as_view(), name="main"),
    url(r'^end', EndView.as_view(), name="dodaj"),
    url(r'^EditUser/(?P<pk>(\d)+)', StreamoorUserUpdate.as_view()),
    url(r'^DeleteUser/(?P<pk>(\d)+)', StreamoorUserDelete.as_view()),
    url(r'^login$', LoginView.as_view()),
    url(r'^logout$', LogoutView.as_view()),
    url(r'^deal$', DealView.as_view()),
    url(r'^User/(?P<pk>(\d)+)', UserProfile.as_view()),
    url(r'^netflix', SearchNetflix.as_view()),
    url(r'^hbo', SearchHBO.as_view()),
    url(r'^amazon', SearchAmazon.as_view()),
    url(r'^home', HomeView.as_view()),
]


