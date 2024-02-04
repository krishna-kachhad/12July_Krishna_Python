from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests

# Create your views here.


@api_view(['GET'])
def getall(request):
    bkdata=bookinfo.objects.all()
    serial=bookserializers(bkdata,many=True)
    return Response(data=serial.data)

@api_view(['GET'])
def getid(request,id):
    try:
        bkid=bookinfo.objects.get(id=id)
    except bookinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serial=bookserializers(bkid)
    return Response(data=serial.data)

@api_view(['DELETE','GET'])
def deleteid(request,id):
    try:
        bkid=bookinfo.objects.get(id=id)
    except bookinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serial=bookserializers(bkid)
        return Response(data=serial.data)
    
    if request.method=='DELETE':
        bookinfo.delete(bkid)
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["POST"])
def insertdata(request):
    if request.method=='POST':
        bkdata=bookserializers(data=request.data)
        if bkdata.is_valid():
            bkdata.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','GET'])
def updatedata(request,id):
    try:
        bkid=bookinfo.objects.get(id=id)
    except bookinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serial=bookserializers(bkid)
        return Response(data=serial.data)

    if request.method=='PUT':
        bkdata=bookserializers(data=request.data,instance=bkid)
        if bkdata.is_valid():
            bkdata.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)