from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import * 

def index(request):
    user = request.user
    tasks = Task.objects.filter(master = user)
    sofi = [0] * 27
    total = [0] * 27
    data = []
    for task in tasks:
        sofi[task.number-1]+= task.state
        total[task.number-1]+= 1
    i=1
    for s,t in zip(sofi,total):
        beep = {
            "p":0 if t==0 else round(s/t*100,1),
            "status": True if t else False,
            "i":i
        }
        i+=1
        data.append(beep)
    template = loader.get_template("base/index.html")
    context = {
        "data": data,
    }
    return HttpResponse(template.render(context, request))

# Create your views here.

