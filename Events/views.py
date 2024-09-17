from django.shortcuts import redirect, render

from Events.models import Events


# Create your views here.
def home(request):
    data = Events.objects.all()
    context = {'data': data}
    return render(request, 'home.html')

def eventedit(request):
    return render(request, 'event_edit.html')

def eventlist(request):

    return render(request, 'event_list.html')

def save(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        date = request.POST.get('date')
        time = request.POST.get('time')
        location = request.POST.get('location')
        attendees = request.POST.get('attendees')
        form = Events(name=name,description=description,date=date,time=time,location=location,attendees=attendees)
        form.save()
        return redirect("/")
    return render(request, 'event_list.html')
