from django.shortcuts import render
from rest_framework.response import Response
from .models import HtmlTutorial, CssTutorial, BootstrapTutorial, JavaScriptTutorial, ReactTutorial
from rest_framework.decorators import api_view
from rest_framework import serializers

# Create your views here.

class HtmlUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = HtmlTutorial
        fields = '__all__'

@api_view(['GET'])
def UploadHtmlVideo(request):
    vid = HtmlTutorial.objects.all()
    serializerData = HtmlUploadSerializer(vid, many=True)

    return Response(serializerData.data)

class CssUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CssTutorial
        fields = '__all__'

@api_view(['GET'])
def UploadCssVideo(request):
    vid = CssTutorial.objects.all()
    serializerData = CssUploadSerializer(vid, many=True)

    return Response(serializerData.data)

class BootstrapUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = BootstrapTutorial
        fields = '__all__'

@api_view(['GET'])
def UploadBootstrapVideo(request):
    vid = BootstrapTutorial.objects.all()
    serializerData = BootstrapUploadSerializer(vid, many=True)

    return Response(serializerData.data)

class JavascriptUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = JavaScriptTutorial
        fields = '__all__'

@api_view(['GET'])
def UploadJavascriptVideo(request):
    vid = JavaScriptTutorial.objects.all()
    serializerData = JavascriptUploadSerializer(vid, many=True)

    return Response(serializerData.data)

class ReactUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReactTutorial
        fields = '__all__'

@api_view(['GET'])
def UploadReactVideo(request):
    vid = ReactTutorial.objects.all()
    serializerData = ReactUploadSerializer(vid, many=True)

    return Response(serializerData.data)