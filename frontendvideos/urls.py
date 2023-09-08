from django.urls import path
from .views import UploadHtmlVideo, UploadCssVideo, UploadBootstrapVideo, UploadJavascriptVideo, UploadReactVideo

urlpatterns = [
    path('htmlvideos/', UploadHtmlVideo),
    path('cssvideos/', UploadCssVideo),
    path('bootstrapvideos/', UploadBootstrapVideo),
    path('javascriptvideos/', UploadJavascriptVideo),
    path('reactvideos/', UploadReactVideo),
]