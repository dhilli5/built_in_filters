from django.shortcuts import render

# Create your views here.
from app.forms import TopicForm
from django.http import HttpResponse


def insert_topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}
    
    if request.method=="POST":
        TFD=TopicForm(request.POST)
        
        if TFD.is_valid():
            TFD.save()
            
            return HttpResponse("data inserted")
        else:
            return HttpResponse("data is not valid")
            
    return render(request,'insert_topic.html',d)
def insert_webpage(request):
    return render(request,'insert_webpage.html')

def filter(request):
    d={"data":"HeLLo hoW Are"}
    return render(request,'filter.html',d)    