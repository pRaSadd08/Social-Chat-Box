from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from.models import Social
from.froms import Form, PictureForm
from django.urls import reverse_lazy, reverse

# Create your views here.
def chat(request):
  if request.method =='POST':
        form = Form(request.POST, request.FILES)
      # if the from is valid
        if form.is_valid(): 
        #yes,Save
          form.save()
        # redirect to home
          return HttpResponseRedirect('/')
        
        #no, Show Error
        else:
          return HttpResponseRedirect(form.errors.as_json())
  chats = Social.objects.all().order_by('DateTime')[:20]
  return render (request, 'chat.html',{'chats':chats})


def edit(request,id):
  chats = Social.objects.get(id=id)
  if request.method == 'POST':
        form = Form(request.POST, request.FILES, instance=chats)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
  return render (request, 'edit.html',{'chats':chats})

def delete(request,id):
  chats=Social.objects.get(id=id)
  chats.delete()
  return HttpResponseRedirect('/')

# def upload(request):
#   chats=Social.objects.get(id=id)
#   if request.method == 'POST':
#         form = Form(request.POST, request.FILES, instance=chats)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/')
#         else:
#             return HttpResponseRedirect(form.errors.as_json())
 
  

def LikeView(request, post_id):
    chats = Social.objects.get(id=post_id)
    new_value = chats.likes+1
    chats.likes = new_value
    chats.save()
    return HttpResponseRedirect('/')
  
  

    