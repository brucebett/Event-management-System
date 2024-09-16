from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def eventedit(request):
    return render(request, 'event_edit.html')

def eventlist(request):
    return render(request, 'event_list.html')