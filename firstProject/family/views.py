from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Family

def index(request):
  myfamily = Family.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'myfamily': myfamily,
  }
  return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  family = Family(firstName=x, lastName=y)
  family.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    family = Family.objects.get(id=id)
    family.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    myfamily = Family.objects.get(id=id)
    template = loader.get_template('update.html')
    context= {
        'myfamily': myfamily,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    family = Family.objects.get(id=id)
    family.firstName = first
    family.lastName = last
    family.save()
    return HttpResponseRedirect(reverse('index'))

# def template(request):
#   template = loader.get_template('template.html')
#   context = {
#     'firstName': 'Dinna'
#   }
#   return HttpResponse(template.render(context, request))

# def template(request):
#   template = loader.get_template('template.html')
#   return HttpResponse(template.render()) 

#to get data from models
def template(request):
  family = Family.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'family': family,
    'firstName': 'Dinna',
    'good': 2,
  }
  return HttpResponse(template.render(context, request))