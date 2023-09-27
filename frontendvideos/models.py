from django.db import models

# Create your models here.
class HtmlTutorial(models.Model):
    tutorialTopic = models.CharField(max_length= 200)
    tutorialVid = models.URLField(max_length= 255)
    tutorialTime = models.IntegerField(default=0)

    def __str__(self):
        return self.tutorialTopic

class CssTutorial(models.Model):
    tutorialTopic = models.CharField(max_length= 200)
    tutorialVid = models.URLField(max_length= 255)
    tutorialTime = models.IntegerField(default=0)

    def __str__(self):
        return self.tutorialTopic

class BootstrapTutorial(models.Model):
    tutorialTopic = models.CharField(max_length= 200)
    tutorialVid = models.URLField(max_length= 255)
    tutorialTime = models.IntegerField(default=0)

    def __str__(self):
        return self.tutorialTopic
    
class JavaScriptTutorial(models.Model):
    tutorialTopic = models.CharField(max_length= 200)
    tutorialVid = models.URLField(max_length= 255)
    tutorialTime = models.IntegerField(default=0)

    def __str__(self):
        return self.tutorialTopic
        
class ReactTutorial(models.Model):
    tutorialTopic = models.CharField(max_length= 200)
    tutorialVid = models.URLField(max_length= 255)
    tutorialTime = models.IntegerField(default=0)

    def __str__(self):
        return self.tutorialTopic