from django.shortcuts import render
from django.http import HttpResponse
from .models import Entry

def index(req):
    entries = Entry.objects.all()
    return render(req, 'myapp/index.html', { 'entries': entries })