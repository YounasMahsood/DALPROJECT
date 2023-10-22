from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def DAL(request):
    return HttpResponse("<h1>Hello this is DAL HomePage.</h1>")

def susses_page(request):
    return HttpResponse("<h1>Hey this is success page</h1>")