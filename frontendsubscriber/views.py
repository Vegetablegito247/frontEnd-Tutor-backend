from rest_framework.response import Response
from .models import Subscriber
from rest_framework.decorators import api_view
from rest_framework import serializers
# Create your views here.

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'

@api_view(['POST'])
def GetSubscriber(request):
    serializeData = SubscriberSerializer(data = request.data)

    if serializeData.is_valid():
        serializeData.save()
        return Response('success')
    else:
        return Response(serializeData.errors)

# +++++++++++ DJANGO +++++++++++
# To use your own Django app use code like this:
import os
import sys

# assuming your Django settings file is at '/home/myusername/mysite/mysite/settings.py'
path = '/home/DoubleA247/frontEnd-Tutor-backend'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'logic.settings'

## Uncomment the lines below depending on your Django version
###### then, for Django >=1.5:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
###### or, for older Django <=1.4
#import django.core.handlers.wsgi