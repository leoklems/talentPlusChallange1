from rest_framework import serializers
from .models import Display


'''
This is going to describe the process of going from a python object to json
'''


class DisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Display
        fields = ('pre', 'major', 'post')