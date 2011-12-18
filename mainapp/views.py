# Create your views here.
from django.contrib.auth.models import User
#from django.forms.forms import Form
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context
from django.shortcuts import render_to_response
from django.contrib.auth import logout
from django.template.context import RequestContext
from mainapp.models import Email

def main_page(request):
    if request.method == 'POST':
        #form = Form(request.POST)
        current_user = User.objects.get(username=request.POST['username'])
        if current_user.password == request.POST['password']:
            variables = Context({
                'user_name': current_user.username
            })
            return render_to_response('main_page.html', variables)
        else:
            return render_to_response('registration/login.html',
                    {'error_message': "Your username and password didn't match. Please try again.",
                     'user_name': current_user.username }, context_instance=RequestContext(request))
    return render_to_response('main_page.html')

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

def compose_mail(request):
    if request.method == 'POST':
        current_user = User.objects.get(username=request.POST['username'])
        composed_email = Email(to_email_id=request.POST['to_id'],from_email_id=current_user.email,subject=request.POST['subject'],content=request.POST['content'])
        composed_email.save()
        return render_to_response('main_page.html',{
                'user_name': current_user.username,
                'success_message': 'Your Email sent successfully'})
    return render_to_response('project/compose_mail.html')
