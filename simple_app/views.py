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
        display: Get all the displays
        serializer: serialize them
    :return: renders a html page with display as json object
    """
    if request.method == 'GET':
        display = Display.objects.all()
        serializer = DisplaySerializer(display, many=True)
        # return Response({"displays": serializer.data})
        print(serializer.data)
        return render(request, 'index.html', {"displays": serializer.data})

    # if request.method == 'POST':
    #     serializer = DisplaySerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status= status.HTTP_201_CREATED)
