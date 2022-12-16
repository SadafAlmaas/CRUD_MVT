from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q

def display_topics(request):
    LTO=Topic.objects.all()
    LTO=Topic.objects.filter(topic_name__startswith='c')
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
    LWO=Webpage.objects.filter(name__startswith='m')
    LWO=Webpage.objects.filter(name__endswith='o')
    LWO=Webpage.objects.filter(name__contains='s')
    LWO=Webpage.objects.filter(name__in=('MSD','Abc'))
    LWO=Webpage.objects.filter(name__regex='^M\w{2}')
    LWO=Webpage.objects.filter(Q(name__startswith='m') & Q(name__endswith='d'))
    LWO=Webpage.objects.filter(Q(name__startswith='m') | Q(name__endswith='o'))
    LWO=Webpage.objects.all()
    d={'LWO':LWO}
    return render(request,'display_webpage.html',d)    

def display_accessrecords(request):
    LAO=AccessRecords.objects.all()
    LAO=AccessRecords.objects.filter(date__month=9)
    LAO=AccessRecords.objects.filter(date__day=4)
    LAO=AccessRecords.objects.filter(date__year=1994)
    LAO=AccessRecords.objects.filter(date__lt='1994-12-15')
    LAO=AccessRecords.objects.filter(date__lte='1994-12-15')
    LAO=AccessRecords.objects.filter(date__gt='1989-09-02')
    LAO=AccessRecords.objects.filter(date__gte='1989-09-02')
   


    d={'LAO':LAO}
    return render(request,'display_accessrecords.html',d)

def update_webpage(request):
    #Webpage.objects.filter(topic_name='Foot Ball').update(name='PQR')
    #Webpage.objects.all().update(topic_name='Volley Ball',name='XYZ',url='https://xyz.in')
    T=Topic.objects.get_or_create(topic_name='Cricket')[0]
    T.save()
    Webpage.objects.update_or_create(name='ABD',defaults={'topic_name':T,'url':'https://ABD.in'})
    LWO=Webpage.objects.all()
    d={'LWO':LWO}
    return render(request,'display_webpage.html',d)

def delete_webpage(request):
    ##Webpage.objects.filter(topic_name='Cricket').delete()
    Webpage.objects.all().delete()  
    LWO=Webpage.objects.all()
    d={'LWO':LWO}
    return render(request,'display_webpage.html',d)