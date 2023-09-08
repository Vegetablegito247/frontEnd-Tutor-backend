from django.shortcuts import render
from rest_framework.response import Response
from .models import HtmlTutorial, CssTutorial, BootstrapTutorial, JavaScriptTutorial, ReactTutorial
from rest_framework.decorators import api_view
from rest_framework import serializers

# Create your views here.

class HtmlUploadSerializer(serializers.Serializer):
    class meta:
        model = HtmlTutorial
        field = '__all__'

@api_view(['GET'])
def UploadHtmlVideo(request):
    vid = HtmlTutorial.objects.all()
    serializerData = HtmlUploadSerializer(vid, many=True)

    return Response(serializerData.data)

class CssUploadSerializer(serializers.Serializer):
    class meta:
        model = CssTutorial
        field = '__all__'

@api_view(['GET'])
def UploadCssVideo(request):
    vid = CssTutorial.objects.all()
    serializerData = CssUploadSerializer(vid, many=True)

    return Response(serializerData.data)

class BootstrapUploadSerializer(serializers.Serializer):
    class meta:
        model = BootstrapTutorial
        field = '__all__'

@api_view(['GET'])
def UploadBootstrapVideo(request):
    vid = BootstrapTutorial.objects.all()
    serializerData = BootstrapUploadSerializer(vid, many=True)

    return Response(serializerData.data)

class JavascriptUploadSerializer(serializers.Serializer):
    class meta:
        model = JavaScriptTutorial
        field = '__all__'

@api_view(['GET'])
def UploadJavascriptVideo(request):
    vid = JavaScriptTutorial.objects.all()
    serializerData = JavascriptUploadSerializer(vid, many=True)

    return Response(serializerData.data)

class ReactUploadSerializer(serializers.Serializer):
    class meta:
        model = ReactTutorial
        field = '__all__'

@api_view(['GET'])
def UploadReactVideo(request):
    vid = ReactTutorial.objects.all()
    serializerData = ReactUploadSerializer(vid, many=True)

    return Response(serializerData.data)