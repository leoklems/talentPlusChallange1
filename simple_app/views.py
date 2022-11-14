from django.shortcuts import render
from django.http import JsonResponse
from .models import Display
from .serializers import DisplaySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
def display_view(request, format=None):
    """
    :param request:
        drinks: Get all the drinks
        serializer: serialize them
    :return: json
    """
    if request.method == 'GET':
        drinks = Display.objects.all()
        serializer = DisplaySerializer(drinks, many=True)
        # return Response({"displays": serializer.data})
        print(serializer.data)
        return render(request, 'index.html', {"displays": serializer.data})
        # return JsonResponse({"Drinks": serializer.data}, safe=False) # When runing the first time

    if request.method == 'POST':
        serializer = DisplaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
