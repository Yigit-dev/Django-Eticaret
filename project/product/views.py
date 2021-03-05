from django.shortcuts import render,HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from product.models import CommentForm, Comment
# Create your views here.

def index(request):  
  return HttpResponse("Product Page")

@login_required(login_url='/login')
def addcomment(request,id):
  url = request.META.get('HTTP_REFERER')
  if request.method == 'POST': #form post edildiyse
    form = CommentForm(request.POST)
    if form.is_valid():
      current_user = request.user # Access user session

      data = Comment() # model ile bağlantı kur
      data.user_id = current_user.id
      data.product_id = id
      data.subject = form.cleaned_data['subject']
      data.comment = form.cleaned_data['comment']
      data.rate = form.cleaned_data['rate']
      data.ip = request.META.get('REMOTE_ADDR') # client computer ip address
      data.save() #veritabanına kaydet
      messages.success(request, "Yorum başarılı şekilde gönderildi")
      return HttpResponseRedirect(url)
      
  messages.danger(request, "İşlem Başarısız")
  return HttpResponseRedirect(url)