from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from.models import Social
from.froms import Form
# Create your views here.
def chat(request):
    if request.method =='POST':
        form = Form(request.POST)
      # if the from is valid
        if form.is_valid(): 
        #yes,Save
          form.save()
        # redirect to home
          return HttpResponseRedirect('/')
        
        #no, Show Error
        else:
          return HttpResponseRedirect(form.errors_as_jason())
    chats = Social.objects.all()
    return render (request, 'chat.html',{'chats':chats})


def edit(request):
  if request.method =='POST':
        form = Form(request.POST)
      # if the from is valid
        if form.is_valid(): 
        #yes,Save
          form.save()
        # redirect to home
          return HttpResponseRedirect('/')
        
        #no, Show Error
        else:
          return HttpResponseRedirect(form.errors_as_jason())
  chats = Social.objects.all()
  return render (request, 'chat.html',{'chats':chats})



    