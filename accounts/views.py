from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.urls import reverse
from .forms import UserLoginForm, UserRegistrationForm
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from .models import userAccounts


# Create your views here.
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


def login(request):
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(username=request.POST['username_or_email'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")

                if request.GET and request.GET['next'] != '':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('profile'))
            else:
                user_form.add_error(None, "Your username or password are incorrect")
    else:
        user_form = UserLoginForm()

    args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            user_name=request.POST.get('username')
            password=request.POST.get('password1')
            user_email=request.POST.get('email')

            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                insertAccount=userAccounts.objects.create(userName=user_name,password=password)
                insertAccount.save()
                messages.success(request, "You have successfully registered")
                from django.core.mail import EmailMessage
                #
                # email = EmailMessage('title', 'body', to=[user_email])
                # email.send()
                # import smtplib
                #
                # FROM = "aryansharma23124@gmail.com"
                # TO = user_email
                # pwd=""
                # SUBJECT = "Registeration"
                # TEXT = "You have been Successfully Registered"
                # server = smtplib.SMTP("smtp.gmail.com", 587)
                # server.ehlo()
                # server.starttls()
                # server.login(FROM, pwd)
                # server.sendmail(FROM, TO,TEXT)
                # server.close()
                if request.GET and request.GET['next'] != '':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect('index')
            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        user_form = UserRegistrationForm()

    args = {'user_form': user_form}
    return render(request, 'register.html', args)


@login_required
def profile(request):
    return render(request, 'profile.html')