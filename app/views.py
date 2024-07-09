from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet

from app.models import *

from app.serializers import *

from rest_framework.response import Response


class ProductCrud(ViewSet):
    def list(self,request):
        LPO=Product.objects.all()#python fomated
        JPO=ProductModelserializers(LPO,many=True)
        return Response(JPO.data)
    
    def retrieve(self,request,pk):
        POD=Product.objects.get(ProductId=pk)
        JO=ProductModelserializers(POD)
        return Response(JO.data)
    
    def create(self,request):
        JDO=request.data
        PDO=ProductModelserializers(data=JDO)
        if PDO.is_valid():
            PDO.save()
            return Response({'create':'data create successfully'})
        else:
            return Response({'failed':'invalid data'})
        
    def update(self,request,pk):
        PDS=Product.objects.get(ProductId=pk)
        PSO=request.data
        JDO=ProductModelserializers(PDS,data=PSO)

        if JDO.is_valid():
            JDO.save()
            return Response({'update':'data update successfully'})
        else:
            return Response({'failed':'data not updated'})
        
    def partial_update(self,request,pk):
        PPO=Product.objects.get(ProductId=pk)
        PSO=request.data
        JDO=ProductModelserializers(PPO,data=PSO,partial=True)

        if JDO.is_valid():
            JDO.save()
            return Response({'update':'data update successfully'})
        else:
            return Response({'failed':'data not updated'})
    
    def delete(self,request,pk):
        PDP=Product.objects.get(ProductId=pk)
        PDP.delete()
        return Response({'delete':'data is deleted successfully'})