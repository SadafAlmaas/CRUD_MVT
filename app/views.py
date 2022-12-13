from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length

def display_topics(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'display_topics.html',d)


def display_webpage(request):
    LWO=Webpage.objects.all()
    LWO=Webpage.objects.all().order_by('name')
    LWO=Webpage.objects.all().order_by('-name')
    LWO=Webpage.objects.filter(topic_name='Cricket')
    LWO=Webpage.objects.exclude(topic_name='Cricket')
    LWO=Webpage.objects.all()[:3:]
    LWO=Webpage.objects.all().order_by(Length('name'))
    LWO=Webpage.objects.all().order_by(Length('name').desc())
    d={'LWO':LWO}
    return render(request,'display_webpage.html',d)    

def display_accessrecords(request):
    LAO=AccessRecords.objects.all()
    d={'LAO':LAO}
    return render(request,'display_accessrecords.html',d)

