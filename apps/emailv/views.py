from django.shortcuts import render, redirect
from .models import Email
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'emailv/index.html' )

def register(request):
    if request.method == 'POST':
        result = Email.objects.add_email(email=request.POST['email'])
        if result[0] == False :
            print "result : ", result[0]
            for error_message in result[1] :
                messages.add_message(request, messages.INFO, error_message)
            return redirect(reverse( 'index' ) )
        else :
            for success_message in result[1] :
                messages.success(request, success_message)
            return redirect(reverse( 'show_emails' ))

def show_emails(request):
    all_emails = Email.objects.getemails()
    context = {
    'all_emails' : all_emails
    }
    return render(request, 'emailv/emails.html', context)

def logout(request):
    request.session.pop('email', None)
    return redirect(reverse( 'index' ) )

def del_prompt(request, id):
    email = Email.objects.get(id=id)
    context = {
    'email' : email
    }
    return render(request, 'emailv/del_prompt.html', context )

def del_email(request, id):
    email = Email.objects.get(id=id)

    Email.objects.filter(id=id).delete()
    return redirect(reverse( 'show_emails' ) )
