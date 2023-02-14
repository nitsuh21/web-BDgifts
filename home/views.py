from django.shortcuts import render,redirect
from home.models import Wish,Video,Gift
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import auth
import random

# Create your views here.
def home(request):
    wishes = Wish.objects.all().order_by('-id')
    print(wishes)
    context = {
        'wishes':wishes
    }
    return render(request,'home.html',context)

def gallery(request):
    return render(request,'gallery.html')

def wishes(request):
    wishes = Wish.objects.all().order_by('-id')
    print(wishes)
    context = {
        'wishes':wishes
    }
    return render(request,'wishes.html',context)

def videos(request):
    videos = Video.objects.all().order_by('-id')
    videos = list(videos)
    random.shuffle(videos)
    print(videos)
    context = {
        'videos':videos
    }
    return render(request,'videos.html',context)

def contactus(request):
    return render(request,'contactus.html')

def makeawish(request):
    if request.method == 'POST':
        name = request.POST['name']
        message = request.POST['message']
        relation = request.POST['relation']
        wish = Wish(name=name,message=message,relation=relation)
        wish.save()
        return redirect('wishes')
    else:
        return render(request,'makeawish.html')
    
def giveagift(request):
    if request.method == 'POST':
        name = request.POST['name']
        gift = request.POST['gift']
        email = request.POST['email']
        gifttype = request.POST['gifttype']
        gift = Gift(name=name,gift=gift,email=email,gifttype=gifttype)
        gift.save()
        return redirect('giveagift')
    else:
        return render(request,'giveagift.html')

def login(request):
	if request.method == 'POST':
		username=request.POST['username']
		password=request.POST['password']
		user=auth.authenticate(request,username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('mygifts')
		else:
			messages.info(request,'These gift are only for hermela')
			return redirect('login')
	else:
		if request.user.is_authenticated:
			return redirect('mygifts')
		else:
			return render(request,'login.html')

def opengift(request,name):
    gift = Gift.objects.get(name=name)
    print(gift.emailed)
    if gift.emailed == 0:
        print(gift.emailed)
        gift.emailed = 1
        print(gift.emailed)
        gift.save()
        send_mail('Gift opened','Hermi just opened your gift','ourtubedevteam@gmail.com',[gift.email],fail_silently=False)
    else:
        pass		
    context = {
        'gift':gift
    }
    return render(request,'gift.html',context)

def mygifts(request):
    print(request.user)
    if request.user.is_authenticated:
        print(request.user)
        gifts = Gift.objects.all()
        print(gifts)
        context={
            'gifts':gifts
        }
        return render(request,'gifts.html',context)
    else:
        return redirect('wishes')
    
