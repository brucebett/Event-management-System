from django.http import JsonResponse
from django.shortcuts import redirect, render

from Events.models import Events
from Events.serializers import EventSerializer


# Create your views here.
def home(request):
    data = Events.objects.all()
    context = {'data': data}
    return render(request, 'home.html', context)

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

def eventedit(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        date = request.POST.get('date')
        time = request.POST.get('time')
        location = request.POST.get('location')
        attendees = request.POST.get('attendees')

        editForm = Events.objects.get(id=id)
        editForm.name = name
        editForm.description = description
        editForm.date = date
        editForm.time = time
        editForm.location = location
        editForm.attendees = attendees
        editForm.save()
        return redirect("/")
    event = Events.objects.all()
    context = {'event': event}
    return render(request, 'event_edit.html', context)

def eventlist(request):
    data = Events.objects.all()
    context = {'data': data}
    return render(request, 'event_list.html', context )




def deleteEvent(request, id):
    event = Events.objects.get(id=id)
    event.delete()
    return redirect("/")


def event_list(request):
    event = Events.objects.all()
    serialize = EventSerializer(event, many=True)
    return JsonResponse(serialize.data, safe=False)