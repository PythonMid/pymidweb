from django.shortcuts import render_to_response, RequestContext, HttpResponseRedirect
from django.contrib.auth import logout

# Create your views here.


def index_view(request):
    return render_to_response('index.html', context=RequestContext(request))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")