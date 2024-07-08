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