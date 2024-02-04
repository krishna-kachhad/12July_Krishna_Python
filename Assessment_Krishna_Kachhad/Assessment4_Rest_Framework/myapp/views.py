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
    cmtdata=comment.objects.all()
    serial=cmtserializers(cmtdata,many=True)
    return Response(data=serial.data)

@api_view(['GET'])
def getid(request,id):
    try:
        cmtid=comment.objects.get(id=id)
    except comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serial=cmtserializers(cmtid)
    return Response(data=serial.data)

@api_view(['DELETE','GET'])
def deleteid(request,id):
    try:
        cmtid=comment.objects.get(id=id)
    except comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serial=cmtserializers(cmtid)
        return Response(data=serial.data)
    
    if request.method=='DELETE':
        comment.delete(cmtid)
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["POST"])
def insertdata(request):
    if request.method=='POST':
        cmtdata=cmtserializers(data=request.data)
        if cmtdata.is_valid():
            cmtdata.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['PUT','GET'])
def updatedata(request,id):
    try:
        cmtid=comment.objects.get(id=id)
    except comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serial=cmtserializers(cmtid)
        return Response(data=serial.data)

    if request.method=='PUT':
        cmtdata=cmtserializers(data=request.data,instance=cmtid)
        if cmtdata.is_valid():
            cmtdata.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)