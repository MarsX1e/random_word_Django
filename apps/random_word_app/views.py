# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.crypto import get_random_string
from django.shortcuts import render,redirect

def index(request):
    if 'number' in request.session:
        print '...'
    else:
        request.session["number"]=1
    randomstr=get_random_string(length=32)
    context={
        "number":request.session['number'],
        "str":randomstr
        }
    return render(request, 'random_word_app/index.html',context)
    
def show(request):

    
    request.session["number"]+=1
    
    return redirect('/')
def reset(request):
    request.session['number']=1
    return redirect('/')

# Create your views here.
# we use form action to redirect to another route(page) to run the function and redirectback so we don't run everythin at
# index. 
