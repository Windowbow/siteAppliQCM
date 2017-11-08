from django.db import models

# Create your models here.
class Question(models.Model):
    UVAssocie = models.CharField(max_length=3, help_text="TC ou ELP par exemple")
    coursAssocie = models.CharField(max_length=4, help_text="121C par exemple")
    question = models.TextField()
    proposition_1 = models.TextField()
    proposition_2 = models.TextField()
    proposition_3 = models.TextField(blank=True, default="")
    proposition_4 = models.TextField(blank=True, default="")
    
    def __str__(self):
        return self.question

class PropQuestion(Question):
    nbValidation = models.IntegerField(default=0)