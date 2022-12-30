from django.shortcuts import render

# Create your views here.
def second(request):
    d={'name':'ram','age':'22'}
    return render(request,'second.html',d)


