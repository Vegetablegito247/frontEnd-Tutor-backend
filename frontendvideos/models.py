from django.db import models

# Create your models here.
class HtmlTutorial(models.Model):
    tutorialTopic = models.CharField(max_length= 200, blank= True)
    tutorialVid = models.FileField(upload_to = 'videos/')

    def __str__(self):
        return self.tutorialVid

class CssTutorial(models.Model):
    tutorialTopic = models.CharField(max_length= 200, blank= True)
    tutorialVid = models.FileField(upload_to = 'videos/')

    def __str__(self):
        return self.tutorialVid

class BootstrapTutorial(models.Model):
    tutorialTopic = models.CharField(max_length= 200, blank= True)
    tutorialVid = models.FileField(upload_to = 'videos/')

    def __str__(self):
        return self.tutorialVid
    
class JavaScriptTutorial(models.Model):
    tutorialTopic = models.CharField(max_length= 200, blank= True)
    tutorialVid = models.FileField(upload_to = 'videos/')

    def __str__(self):
        return self.tutorialVid
        
class ReactTutorial(models.Model):
    tutorialTopic = models.CharField(max_length= 200, blank= True)
    tutorialVid = models.FileField(upload_to = 'videos/')

    def __str__(self):
        return self.tutorialVid