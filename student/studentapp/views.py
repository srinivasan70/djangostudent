from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from studentapp.models import studentmarks
from studentapp.serializers import studentmarklistSerializer
import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class post_data(APIView):
    @csrf_exempt
           
    def post(self,request):
        try:
            
            request_data=request.data
            print(request_data)
        
            rollno=request_data['data']['rollno']
            name=request_data['data']['name']
            mark1=request_data['data']['mark1']
            mark2=request_data['data']['mark2']
            mark3=request_data['data']['mark3']
            mark4=request_data['data']['mark4']
            mark5=request_data['data']['mark5']

            studentmarks.objects.create(rollno=rollno,name=name,mark1=mark1,mark2=mark2,mark3=mark3,mark4=mark4,mark5=mark5)
            '''
            studentmarks1=studentmarks(rollno,name,mark1,mark2,mark3,mark4,mark5)
            print(studentmarks1)
            studentmarks1.save()
            studentmarks1.objects.all()
            '''

            studentmarks1= studentmarks.objects.filter(rollno=rollno).first()
            print(studentmarks1)
            if (studentmarks1!=None):
                return Response(status=status.HTTP_200_OK, data={"remarks":'Marks Created Successfully'})
            else:
                return Response(status =status.HTTP_400_BAD_REQUEST, data={"remarks":'Data not created'})

        except:
            print("Error")

class displaymark(APIView):
    @csrf_exempt
    def post(self,request):
        try:
            request_data=request.data
            print(request_data)
            rollno=request_data['data']['rollno']
            print(rollno)

            studentmarks1= studentmarks.objects.filter(rollno=rollno).first()
            print(studentmarks1)
            if(studentmarks1!=None):
                name=studentmarks1.name
                mark1=studentmarks1.mark1
                mark2=studentmarks1.mark2
                mark3=studentmarks1.mark3
                mark4=studentmarks1.mark4
                mark5=studentmarks1.mark5

                print(name)
                print(mark1)
                print(mark2)
                print(mark3)
                print(mark4)
                print(mark5)

                return Response(status=status.HTTP_200_OK, data={"name":name,"mark1":mark1,"mark2":mark2,"mark3":mark3,"mark4":mark4,"mark5":mark5})
            else:

                return Response(status =status.HTTP_400_BAD_REQUEST, data={"remarks":'Data not created'})
                
        except:
            print("Error")

class displaymarklist(APIView):
    @csrf_exempt
    def get(self,request):
        try:
            print("Inside get")
            studentmark_list=studentmarks.objects.all()
            print(studentmark_list)
            '''for studentmarks in studentmark_list:
                print(studentmarks.name)'''
            
            print(type(studentmark_list))
            serializer=studentmarklistSerializer(studentmark_list,many=True)
            print(serializer)
            
                    
            
            
            return Response(status=status.HTTP_200_OK, data={"studentmarklist":serializer.data})
        except:
            print("Error")
            

                

            

            
            
            
