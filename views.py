from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Stock
from .serializer import StockSerializer

# list all stock or create a new one
# Stocks/
class StockList(APIView):

    def get(self,request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)


    def post(self):
        pass















