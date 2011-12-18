# Create your views here.
from django.contrib.auth.models import User
#from django.forms.forms import Form
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context
from django.shortcuts import render_to_response
from django.contrib.auth import logout
from django.template.context import RequestContext

def main_page(request):
    if request.method == 'GET':
        return render_to_response('main_page.html')
    if request.method == 'POST':
        #form = Form(request.POST)
        current_user = User.objects.get(username=request.POST['username'])
        if current_user.password == request.POST['password']:
            variables = Context({
                'head_title': u'Mailing System',
                'page_title': u'Welcome to NewMail',
                'page_body': u'Here you can receive & send emails',
                'user_name': current_user.username
            })
            return render_to_response('main_page.html', variables)
        else:
            return render_to_response('registration/login.html',
                    {'error_message': "Your username and password didn't match. Please try again.",
                     'user_name': current_user.username
                #    , 'form':form
                },
                     context_instance=RequestContext(request))

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')