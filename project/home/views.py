from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
# Create your views here.
from home.models import Setting, ContactFormu, ContactFormMessage
from product.models import Product, Category, Images, Comment
from home.forms import SearchForm, SignUpForm
from home.forms import ImageForm, ImageEditForm
from home.models import Image
import cv2
import numpy as np
from matplotlib import pyplot as plt


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Product.objects.all()[:4]
    category = Category.objects.all()
    dayproducts = Product.objects.all()[:4]
    lastproducts = Product.objects.all().order_by('-id')[:4]
    randomproducts = Product.objects.all().order_by('?')[:4]

    context = {'setting': setting,
               'page': 'home',
               'sliderdata': sliderdata,
               'category': category,
               'dayproducts': dayproducts,
               'lastproducts': lastproducts,
               'randomproducts': randomproducts}  # eğer sayfaya değişken göndereceksek context içinde tanımlıyoruz
    return render(request, 'index.html', context)


def hakkimizda(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'category': category, 'setting': setting, }
    return render(request, 'hakkimizda.html', context)


def referanslar(request):
    category = Category.objects.all()

    setting = Setting.objects.get(pk=1)
    context = {'category': category, 'setting': setting}
    return render(request, 'referanslarimiz.html', context)


def iletisim(request):
    if request.method == 'POST':  # form post edildiyse
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()  # model ile bağlantı kur
            data.name = form.cleaned_data['name']  # formdan bilgiyi al
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  # veritabanına kaydet
            messages.success(
                request, "Mesajınız Başarılı Bir Şekilde Gönderildi.")
            return HttpResponseRedirect('/iletisim')
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    context = {'category': category, 'setting': setting, 'form': form}
    return render(request, 'iletisim.html', context)


def category_products(request, id, slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    products = Product.objects.filter(category_id=id)
    context = {
        'products': products,
        'category': category,
        'categorydata': categorydata
    }
    return render(request, 'products.html', context)


def product_detail(request, id, slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id, status='True')
    context = {
        'product': product,
        'category': category,
        'images': images,
        'comments': comments,
    }
    return render(request, 'product_detail.html', context)


def product_search(request):
    if request.method == 'POST':  # form post edildiyse
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query']  # formdan bilgiyi al
            # select* from product where title like %query%
            products = Product.objects.filter(title__icontains=query)
            context = {
                'products': products,
                'category': category,
            }
            return render(request, 'products_search.html', context)

    return HttpResponseRedirect('/')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Giriş Hatası!")
            return HttpResponseRedirect('/login')

    category = Category.objects.all()
    context = {
        'category': category,
    }
    return render(request, 'login.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect("/")

    form = SignUpForm()
    category = Category.objects.all()
    context = {'category': category, 'form': form, }
    return render(request, 'signup.html', context)


def OpencvView(request):
    images = Image.objects.all()
    context = {
        "images": images
    }
    return render(request, 'selectop.html', context)


def CreateImageView(request):
    form = ImageForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('./')
    context = {
        "form":form
    }
    return render(request, "imageadd.html", context)

def EditCv2ImageView(request, id):
    form = ImageEditForm(request.POST or None,request.FILES or None)
    image = Image.objects.get(id=id)
    if form.is_valid():
        image = Image.objects.get(id=id)
        img_main  = cv2.imread(image.image.path, cv2.IMREAD_GRAYSCALE)
        thresh = form.cleaned_data['thresh']
        candidate_img = cv2.threshold(img_main, thresh, 255, cv2.THRESH_BINARY)[1]
        cv2.imwrite(image.modified_image.path, candidate_img)

        #*********

        return HttpResponseRedirect('./')
    context = {
        "form" : form,
        "image" : image
    }
    return render(request, "imageedit.html", context)
