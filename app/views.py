from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.core.mail import send_mail
from app.forms import *

def sendmail(request):
    d={'UFO':UserForm(),'PFO':ProfileForm()}
    if request.method=='POST' and request.FILES:
        UFD=UserForm(request.POST)
        PFD=ProfileForm(request.POST,request.FILES)
        if UFD.is_valid() and PFD.is_valid():
            NSUFO=UFD.save(commit=False)
            pushpswd=UFD.cleaned_data['password']
            NSUFO.set_password(pushpswd)
            NSUFO.save()
            NSPFO=PFD.save(commit=False)
            NSPFO.username=NSUFO
            NSPFO.save()
            send_mail('Registration','Your Registration is Successfully done in Django Project-App','gowdagirishv@gmail.com',
                        [NSUFO.email],fail_silently=False)
            return HttpResponse('Registration Send Mail Successfully done')
        else:
            return HttpResponse('Invalid Data Entered')
    return render(request,'sendmail.html',d)