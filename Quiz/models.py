from django.db import models

# Create your models here.
class Subject(models.Model):
    sub = models.CharField(max_length=50)

    def __str__(self):
        return self.sub

class Question(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    ques = models.CharField(max_length=50)
    ans1 = models.CharField(max_length=50)
    ans2 = models.CharField(max_length=50)
    ans3 = models.CharField(max_length=50)
    ans4 = models.CharField(max_length=50)
    ans = models.CharField(max_length=50)

    def __str__(self):
        return self.ques +' --- '+self.ans1+' ---'+ self.ans2+' ---- '+self.ans3+' --- '+self.ans4+' --- '+ self.ans+' --- '+self.subject.sub
