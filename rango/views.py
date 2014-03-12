from django.template import RequestContext
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
# Create your views here.
def index(request):
    context = RequestContext(request)
    
    context_dict = {'boldmessage': "I am bold font from the context"}
    
    return render_to_response('rango/index.html', context_dict, context)

def about(request):
    context = RequestContext(request)
    
    context_dict = {'boldmessage': "I am bold font form the context"}
    
    return render_to_response('rango/about.html', context_dict, context)
    #return HttpResponse("Rango says: Here is the about page. <a href='/rango'>Index</a>")
