from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm, TextInput, Textarea
# Create your models here.
class Setting(models.Model):
  STATUS = (
    ('True', 'Evet'),
    ('False','Hayır'),
  )
  title = models.CharField(max_length = 100)
  keywords = models.CharField(max_length = 255)
  description = models.CharField(max_length = 255)
  company = models.CharField(max_length = 100)
  address = models.CharField(blank = True, max_length = 100)
  phone = models.CharField(blank = True, max_length = 15)
  fax = models.CharField(blank = True, max_length = 15)
  email = models.CharField(blank = True,max_length = 50)
  smtp_server = models.CharField(blank = True, max_length = 20)
  smtp_email = models.CharField(blank = True, max_length = 20)
  smtp_password = models.CharField(blank = True, max_length = 10)
  smtp_port = models.CharField(blank = True,max_length = 5)
  icon = models.ImageField(blank = True, upload_to = 'images/')
  facebook = models.CharField(blank = True, max_length = 50)
  instagram = models.CharField(blank = True, max_length = 50)
  twitter = models.CharField(blank = True, max_length = 50)
  about_us = RichTextUploadingField(blank = True)
  contact = RichTextUploadingField(blank = True)
  referances = RichTextUploadingField(blank = True)
  status = models.CharField(max_length = 10, choices = STATUS)
  create_at = models.DateTimeField(auto_now_add = True)
  update_at = models.DateTimeField(auto_now = True)

  def __str__(self):
    return self.title

class ContactFormMessage(models.Model):
  STATUS = (
    ('New', 'New'),
    ('Read', 'Read'),
    ('closed','Closed'),
  )
  name = models.CharField(blank = True, max_length = 20)
  email = models.CharField(blank = True, max_length = 50)
  subject = models.CharField(blank = True, max_length = 50)
  message = models.CharField(blank = True, max_length = 255)
  status = models.CharField(max_length=10, choices=STATUS,default='New')
  ip = models.CharField(blank = True, max_length = 20)
  note = models.CharField(blank=True,max_length=100)
  create_at = models.DateTimeField(auto_now_add = True)
  update_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class ContactFormu(ModelForm):
  class Meta:
    model = ContactFormMessage
    fields = ['name','email','subject','message']
    widgets = {
      'name' : TextInput(attrs={'class':'input','placeholder':'Name & Surname'}),
      'subject' : TextInput(attrs={'class':'input','placeholder':'Subject'}),
      'email' : TextInput(attrs={'class':'input','placeholder':'Email Address'}),
      'message' : Textarea(attrs={'class':'input','placeholder':'Your Message','rows':'5'}),
    }

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(null=False, max_length=40)
    modified_image = models.ImageField(upload_to='modified_images/', null=True, blank=True)
    
    def __str__(self):
        return self.title

    def save(self):
        self.modified_image.save(self.image.name, self.image, save=False)
        super(Image, self).save()

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'