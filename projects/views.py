from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def projects(request):
    return render(request, 'projects/projects.html')
    #return HttpResponse("something something")