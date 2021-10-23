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
from django.db.models import Avg,Max,Min


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
            print(serializer.data)
            print(type(serializer.data))
            serializerdict=serializer.data
            print(serializerdict)
            '''json_data=JsonRenderer().renderer(serializer.data)
            print(json_data)
            return JsonResponse(serializer.data,safe=false)'''
            json_data=JSONRenderer().render(serializer.data)
            print(json_data)
            resultdict={}
            for data in serializerdict:
                
                rollno=data['rollno']
                
                print(rollno)
                print(data)
                name=data['name']
                mark1=data['mark1']
                mark2=data['mark2']
                mark3=data['mark3']
                mark4=data['mark4']
                mark5=data['mark5']
                '''
                rollno=data.rollno
                print(rollno)
                name=data.name
                mark1=data.mark1
                mark2=data.mark2
                mark3=data.mark3
                mark4=data.mark3
                mark5=data.mark4 '''
                
                total=mark1+mark2+mark3+mark4+mark5
                print(rollno,name,mark1,mark2,mark3,mark4,mark5,total)

                '''resultdict=[{'Rollno':rollno,'Name':name,'M1':mark1,'M2':mark2,'M3':mark3,'M4':mark4,'M5':mark5,'Total':total}]'''
                resultdict["ROLLNO"]=rollno
                resultdict["M1"]=mark1
                resultdict["M2"]=mark2
                resultdict["M3"]=mark3
                resultdict["M4"]=mark4
                resultdict["M5"]=mark5
                resultdict["total"]=total
                print(resultdict)
                for i in resultdict:
                    print(resultdict[i])
                '''return Response(status=status.HTTP_200_OK, data={"studentmarklist":serializerdict})'''
                    
                
                '''json_obj=[("ROLLNO"=rollno,"NAME"=name,"MARK1"=mark1,"MARK2"=mark2,"MARK3"=mark3,"MARK4"=mark4,"MARK5"=mark5,"TOTAL"=total)]
                    print(json_obj)'''
                    
                
                '''resultdict.update({"ROLLNO":rollno,"NAME":name,"MARK1":mark1,"MARK2":mark2,"MARK3":mark3,"MARK4":mark4,"MARK5":mark5,"TOTAL":total})'''
                
            '''resultdict['ROLLNO'].append(rollno)
            resultdict['NAME'].append(name)
            resultdict['MARK1'].append(mark1)
            resultdict['MARK2'].append(mark2)
            resultdict['MARK3'].append(mark3)
            resultdict['MARK4'].append(mark4)
            resultdict['MARK5'].append(mark5)
            resultdict['TOTAL'].append(total)'''

            '''print(resultdict) '''              
            
                    
            
            
            return Response(status=status.HTTP_200_OK, data={"studentmarklist":resultdict}) 
        except Exception as e:
            print("Error",str(e))
            
class displayaverage(APIView):
    @csrf_exempt
    def get(self,request):
        try:
            print("Inside get")
            student_avg=studentmarks.objects.all()
            print(student_avg)
            print(type(student_avg))
            serializer=studentmarklistSerializer(student_avg,many=True)
            print(serializer)
            print(serializer.data)
            print(type(serializer.data))
            serializerdict=serializer.data
            print(serializerdict)
            resultdict={}
            avg_mark1=student_avg.aggregate(Avg("mark1"))
            print(avg_mark1)
            avg_mark2=student_avg.aggregate(Avg("mark2"))
            print(avg_mark2)
            avg_mark3=student_avg.aggregate(Avg("mark3"))
            print(avg_mark3)
            avg_mark4=student_avg.aggregate(Avg("mark4"))
            print(avg_mark4)
            avg_mark5=student_avg.aggregate(Avg("mark5"))
            print(avg_mark5)
            '''
            resultdict.append({'AVGM1':avg_mark1})
            resultdict.append({'AVGM2':avg_mark2})
            resultdict.append({'AVGM3':avg_mark3})
            resultdict.append({'AVGM4':avg_mark4})
            resultdict.append({'AVGM5':avg_mark5})'''
            
            '''
            avg_mark2=serializer.aggregate(Avg(data['mark2']))
            avg_mark3=serializer.aggregate(Avg(data['mark3']))
            avg_mark4=serializer.aggregate(Avg(data['mark4']))
            avg_mark5=serializer.aggregate(Avg(data['mark5']))
            '''

            '''resultdict[{'AvgM1':avg_mark1,'AVGM2':avg_mark2,'AVGM3':avg_mark3,'AVGM4':avg_mark4,'AVGM5':avg_mark5}]'''
            return Response(status=status.HTTP_200_OK, data=(avg_mark1,avg_mark2,avg_mark3,avg_mark4,avg_mark5))
            '''return Response(status=status.HTTP_200_OK, data=resultdict)'''
        except Exception as e:
            print("Error",str(e))
                

            

            
            
            
