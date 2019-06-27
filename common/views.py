from django.http import HttpResponse
from django.template import loader

from .models import Student, Contact
from .forms import ContactForm

def homepage(request):

  template=loader.get_template('home.html')
  data ={}
  return HttpResponse(template.render(data,request))


def mypage1(request):

  template=loader.get_template('page1.html')
  data ={}
  return HttpResponse(template.render(data,request))



def mypage2(request):

  template=loader.get_template('page2.html')
  data ={}
  return HttpResponse(template.render(data,request))

def resultpage (req):
  template = loader.get_template("result.html")

  data= {"year": 2015,
         "name": "Anil",
         "mark" : 450,
         "status": "PASS"}

  return HttpResponse(template.render(data, req))


def studentinfo (request):
  template = loader.get_template('studentinfo.html')

  aaa = Student.objects.all()

  data = {"sss": aaa}
  return HttpResponse(template.render(data, request))


def contactpage(request):

  if request.method =='POST':

    print (">>>>", request.POST)

    form = ContactForm(request.POST)

    if form.is_valid():

      name= form.cleaned_data['name']
      phone = form.cleaned_data['phone']
      email = form.cleaned_data['email']
      message = form.cleaned_data['message']

      print ("name --", name)
      print ("phone --", phone)
      print ("email--", email)
      print ("messge--", message)

      contact = Contact()
      contact.name= name
      contact.email= email
      contact.phone = phone
      contact.message = message
      contact.save()

      template = loader.get_template('contactsuccess.html')
      data = {"name":name, "email": email}
      return HttpResponse(template.render(data, request))


  else :
    template = loader.get_template('contact.html')
    mycontactform = ContactForm()
    data = {"myform": mycontactform}

    return HttpResponse(template.render(data, request))














