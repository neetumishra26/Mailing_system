# Create your views here.
from django.http import HttpResponseRedirect
from django.template import Context
from django.shortcuts import render_to_response
from django.contrib.auth import logout

def main_page(request):
    variables = Context({
        'head_title':u'Mailing System',
        'page_title':u'Welcome to NewMail',
        'page_body': u'Here you can receive & send emails',
        'user':request.user
    })
    return render_to_response('main_page.html',variables)

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')