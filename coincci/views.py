from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.conf import settings


# Create your views here.
def main(request):
    return render(request, 'Ali/main.html')