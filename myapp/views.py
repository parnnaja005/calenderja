from django.shortcuts import render
from django.http import HttpResponse
from .models import Entry

def index(req):
    entries = Entry.objects.all()
    return render(req, 'myapp/index.html', { 'entries': entries })

def input(req):
    if req.method == 'POST':
        post = req.POST
        s = Entry()
        s.name = post['name']
        s.description = post['description']
        s.save()
        entries = Entry.objects.all()
        print(entries)
        return render(req, 'myapp/input.html', { 'entries': entries })
    else:
        print('ร้องขอทำมะดา')
        entries = Entry.objects.all()
        print(entries)
        return render(req, 'myapp/input.html', {'entries': entries})

def home(req):
    return render(req, 'myapp/home.html')