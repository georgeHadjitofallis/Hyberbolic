#from django.http import HttpResponse
from django.shortcuts import render
#from django.template import loader

def index(request):
    context = {}
    #template = loader.get_template('hyperbolic/home.html')
    #return HttpResponse(template.render(context, request))
    return render(request, './hyperbolic/index.html', context)