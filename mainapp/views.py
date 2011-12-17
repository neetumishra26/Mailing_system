# Create your views here.
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

def main_page(request):
    template = get_template('main_page.html')
    variables = Context({
        'head_title':u'Mailing System',
        'page_title':u'Welcome to Gmail',
        'page_body': u'Here you can receive & send emails'
    })
    output = template.render(variables)
    return HttpResponse(output)
