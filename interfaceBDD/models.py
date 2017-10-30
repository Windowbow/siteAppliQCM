from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.TextField()
    proposition_1 = models.TextField()
    proposition_2 = models.TextField()
    proposition_3 = models.TextField(null=True)
    proposition_4 = models.TextField(null=True)
    
    def __str__(self):
        return self.question
