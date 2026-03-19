from django.shortcuts import render


def home(request):
    return render(request, "home.html")

    
def calculator_home(request):
    buttons = ['7','8','9','/','4','5','6','*','1','2','3','-','0','.','=','+']
    return render(request, "calc/index.html", {"buttons": buttons})
