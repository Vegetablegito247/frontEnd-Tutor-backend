from rest_framework.response import Response
from .models import Subscriber
from rest_framework.decorators import api_view
from rest_framework import serializers
# Create your views here.

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'

@api_view(['POST', 'GET'])
def GetSubscriber(request):
    if request.method == 'POST':
        serializeData = SubscriberSerializer(data = request.data)

        if serializeData.is_valid():
            serializeData.save()
            return Response('success')
        else:
            return Response(serializeData.errors)
    elif request.method == 'GET':
        sub = Subscriber.objects.all()
        serializerdata = SubscriberSerializer(sub, many=True)

        return Response(serializerdata.data)
