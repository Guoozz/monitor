from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def get_warn(request):
    return HttpResponse('i am warn')

def get_flow(request):
    room = request.GET.get('room')
    return HttpResponse({'fuck':'you'})

def get_message(request):

    _type = request.GET.get('type',None)
    title = request.GET.get('title',None)
    content = request.GET.get('content',None)
    is_blcok = request.GET.get('isBlock',False)
    ip = request.GET.get('ip',None)
    referer = request.GET.get('referer',None)
    
    return HttpResponse('i am message')

def dashboard(request):
    
    return render(request,'monitor_chart/dashboard.html')
