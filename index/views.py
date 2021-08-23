import json
from django.shortcuts import render
from .models import Room


def index(request):
    return render(request, 'index/index.html')


def introduce(request):
    return render(request, 'index/introduce.html')


def room(request):
    return render(request, 'index/room_info.html')


def travel(request):
    return render(request, 'index/travel_info.html')


def fac(request):
    return render(request, 'index/fac_info.html')


def reservation(request):
    return render(request, 'index/reservation.html')


def location(request):
    return render(request, 'index/location.html')


def reservating(request):
    return render(request, 'index/reservating.html')


def reservating2(request):
    return render(request, 'index/reservating2.html')


def reserve(request):
    year = request.GET.get('year','0')
    month = request.GET.get('month','13')
    date = request.GET.get('date','32')
    roomN = request.GET.get('roomN','000')
    rooms = Room.objects.all()
    context={'year':year,'month' :month,'date':date,'Sroom':roomN , 'rooms':rooms ,'room_js':json.dumps([room.to_json() for room in rooms])}
    return render(request,'index/reserve.html',context)


def charge_info(request):
    return render(request, 'index/charge_info.html')


def test(request):
    return render(request, 'index/test.html')


def popup(request):
    return render(request, 'index/popuppage.html')



def room101(request):
    return render(request, 'index/room/101.html')


def room201(request):
    return render(request, 'index/room/201.html')


def room301(request):
    return render(request, 'index/room/301.html')
