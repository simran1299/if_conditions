from django.shortcuts import render

# Create your views here.
def if_cond(request):
    d={'a':100}
    return render(request,'if_cond.html',d)

def if_else_cond(request):
    d={'a':100,'b':200}
    return render(request,'if_else_cond.html',d)

def nested_if(request):
    d={'a':100, 'b':200, 'c':300}
    return render(request,'nested_if.html',d)

def elif_cond(request):
    d={'a':100, 'b':200, 'c':300}
    return render(request,'elif_cond.html',d)