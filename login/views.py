# Create your views here.
from django.http import HttpResponse

def login(request):
    #for get method show form, for post method  authorize user
    if request.method == 'GET':
        output = u'''
                <html>
                    <head><title>%s</title></head>
                    <body>
                        <h1>%s</h1>
                    </body>
                </html>
                ''' % (u'Login', u'Login page')
        return HttpResponse(output)