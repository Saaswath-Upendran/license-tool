from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView,TemplateView
from .forms import *
from django.urls import reverse_lazy
from Crypto.Cipher import AES
from django.contrib import messages

# Create your views here.

class HomeView(TemplateView):
    template_name = "index.html"


class UserM(CreateView):
    context_object_name = "form"
    form_class = UserForm
    success_url = reverse_lazy('authapp:home')
    template_name = "register.html"



def fileopener(request):
    if request.method == 'POST':
        form = FileForm(request.POST,request.FILES or None)
        if form.is_valid():
            file = form.cleaned_data['file_upload']
            key = form.cleaned_data['key']
            f = open(str(file),"rb").read()
            key = open(str(key),'rb').read()
            cipher = AES.new(key,AES.MODE_EAX)
            plaintext = cipher.decrypt(f)
            return HttpResponse("You are licensed")
        else:
            return HttpResponse(form.errors)
    else:
        form = FileForm()
        return render(request,'userprofile.html',{'form':form})



