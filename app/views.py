from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet

from app.models import *

from app.serializers import *

from rest_framework.response import Response


class ProductCrud(ViewSet):
    def list(self,request):
        LPO=Product.objects.all()
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