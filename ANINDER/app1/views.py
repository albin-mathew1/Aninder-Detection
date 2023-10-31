import json
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import login,forest_department_login,camera,add_camera_location,suggestions,report_intrusion
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
from django.http import JsonResponse

@csrf_exempt
def HomePage(request):
    if request.method=='POST':
        Mobile_Number=request.POST['Mobile_Number']
        Latitude=request.POST['lat']
        Longitude=request.POST['lng']
        if Latitude=='':
           i=1
           context = {'loc': i}
           return render(request, 'login.html',context)
        if len(Mobile_Number)!=13:
           i=1
           context = {'data': i}
           return render(request, 'login.html',context)
        pattern = re.compile(r'^\+91[6-9]\d{9}$')
        if pattern.match(Mobile_Number):
           try:
               user =login.objects.get(Mobile_Number=Mobile_Number)
               user.Latitude=Latitude
               user.Longitude=Longitude
               user.save()
               return user_home(request)
           except login.DoesNotExist:
                Login=login.objects.create(Mobile_Number = Mobile_Number,Latitude=Latitude,Longitude=Longitude)
                Login.save()
                return user_home(request)
        else:
           i=1
           context = {'data': i}
           return render(request, 'login.html',context)
    return render (request,'login.html')

@csrf_exempt
def SignupPage(request):
    if request.method=='POST':
        Name=request.POST['Name']
        Division=request.POST['Division']
        Designation=request.POST['Designation']
        Email=request.POST['Email']
        forest=forest_department_login.objects.create(Name=Name,Division=Division,Designation=Designation,Email=Email)
        forest.save()
        return forest_home(request)
    return render (request,'forest_department_login.html')

@csrf_exempt
def user_home(request):
    kan_url = 'https://news.google.com/search?q=kerala%20forest%20news&hl=en-IN&gl=IN&ceid=IN%3Aen'
    kan_page = requests.get(kan_url).text
    kan_soup = BeautifulSoup(kan_page, 'html.parser')
    result_t = kan_soup.select('article .DY5T1d.RZIKme')
    kan_news = [t.text for t in result_t]
    kan_links = []
    base_url = kan_url
    for i in kan_soup.select('article .DY5T1d.RZIKme'):
        ss = urljoin(base_url, i.get('href'))
        kan_links.append(ss)
    aik_url = 'https://news.google.com/search?q=animal%20intrusion%20kerala&hl=en-IN&gl=IN&ceid=IN%3Aen'
    aik_page = requests.get(aik_url).text
    aik_soup = BeautifulSoup(aik_page, 'html.parser')
    result_tl = aik_soup.select('article .DY5T1d.RZIKme')
    aik_news = [t.text for t in result_tl]
    aik_links = []
    base_url = aik_url
    for i in aik_soup.select('article .DY5T1d.RZIKme'):
        ss = urljoin(base_url, i.get('href'))
        aik_links.append(ss)
    kan = zip(kan_news, kan_links)
    aik=zip(aik_news, aik_links)
    context = {
        'kan': kan,
        'aik': aik,
    }
    return render(request, 'user_home.html',context)

@csrf_exempt
def forest_home(request):
    kan_url = 'https://news.google.com/search?q=kerala%20forest%20news&hl=en-IN&gl=IN&ceid=IN%3Aen'
    kan_page = requests.get(kan_url).text
    kan_soup = BeautifulSoup(kan_page, 'html.parser')
    result_t = kan_soup.select('article .DY5T1d.RZIKme')
    kan_news = [t.text for t in result_t]
    kan_links = []
    base_url = kan_url
    for i in kan_soup.select('article .DY5T1d.RZIKme'):
        ss = urljoin(base_url, i.get('href'))
        kan_links.append(ss)
    aik_url = 'https://news.google.com/search?q=animal%20intrusion%20kerala&hl=en-IN&gl=IN&ceid=IN%3Aen'
    aik_page = requests.get(aik_url).text
    aik_soup = BeautifulSoup(aik_page, 'html.parser')
    result_tl = aik_soup.select('article .DY5T1d.RZIKme')
    aik_news = [t.text for t in result_tl]
    aik_links = []
    base_url = aik_url
    for i in aik_soup.select('article .DY5T1d.RZIKme'):
        ss = urljoin(base_url, i.get('href'))
        aik_links.append(ss)
    kan = zip(kan_news, kan_links)
    aik=zip(aik_news, aik_links)
    context = {
        'kan': kan,
        'aik': aik,
    }
    return render(request, 'forest_home.html',context)

@csrf_exempt
def report(request):
    return render(request,'report.html')

@csrf_exempt
def get_markers(request):
    camera_locations = camera.objects.filter(CAM_ID__in=add_camera_location.objects.values_list('CAM_ID', flat=True))
    markers = []
    for location in camera_locations:
        camera_location = add_camera_location.objects.get(CAM_ID=location.CAM_ID)
        marker = {
            "Location":camera_location.Location,
            "latitude": camera_location.latitude,
            "longitude": camera_location.longitude,
            "animal": location.Animal,
            "datetime": location.Datetime,
        }

        markers.append(marker)
        markers_json = json.dumps(markers)
        return render(request, 'user_map.html', {'markers': markers_json})
    return render(request, 'user_map.html')

@csrf_exempt
def forest_map(request):
    labels = camera.objects.all()
    context = {'labels': labels}
    return render(request, 'forest_map.html',context)

@csrf_exempt
def addcameraLocation(request):
    if request.method == 'POST':
       CAM_ID=request.POST['name']
       Location=request.POST['Location']
       latitude = request.POST['latitude']
       longitude = request.POST['longitude']
       cameraLocation=add_camera_location.objects.create(CAM_ID=CAM_ID,Location=Location,latitude=latitude,longitude=longitude)
       cameraLocation.save()
       return render(request, 'addcameraLocation.html')
    return render(request, 'addcameraLocation.html')

@csrf_exempt
def suggestions(request):
    if request.method == ['POST']:
        Name=request.POST['Name']
        Designation=request.POST['Designation']
        Email=request.POST['Email']
        suggestion=request.POST['textarea']
        suggest=suggestions.objects.create(Name=Name,Designation=Designation,Email=Email,suggestions=suggestion)
        suggest.save()
        return render(request,'suggest.html')
    return render(request,'suggest.html')


