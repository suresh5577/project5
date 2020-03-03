from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render,HttpResponse
from django.core.mail import EmailMessage

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def sendEmail(request):
    mail_body = "<h1>This is the second email from django!</h1>"
    msg = EmailMessage("welcome suresh", mail_body,'sureshsatyawadaeee@gmail.com',['sureshsurya5577@gmail.com', 'satyawada.mahesh@gmail.com'])
    msg.content_subtype = "html"
    msg.send()

    return HttpResponse("mail sent succeesfully")

def forgetPassword(request):
    return render(request,'forgetpassword.html')

