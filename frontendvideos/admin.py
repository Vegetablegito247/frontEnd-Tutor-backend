from django.contrib import admin
from .models import HtmlTutorial, CssTutorial, BootstrapTutorial, JavaScriptTutorial, ReactTutorial
# Register your models here.

admin.site.register(HtmlTutorial)
admin.site.register(CssTutorial)
admin.site.register(BootstrapTutorial)
admin.site.register(JavaScriptTutorial)
admin.site.register(ReactTutorial)