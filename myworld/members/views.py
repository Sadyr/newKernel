from django.http import HttpResponse
from django.template import loader
from .models import Members

""" def index(request):
    return HttpResponse("Hello world")

def index(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render()) """

def index(request):
    mymembers = Members.objects.all().values()
    output=""
    for x in mymembers:
        output += x["firstname"]
        output += ' '
        output += x["lastname"]

        
    print(output)
    return HttpResponse(output)

