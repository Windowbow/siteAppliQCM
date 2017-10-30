from datetime import datetime
from django.shortcuts import render
from .models import Question
from .forms import PropositionForm

def date_actuelle(request):
    return render(request, 'interfaceBDD/date.html', {'date': datetime.now()})

def home(request):
    questions = Question.objects.all()
    return render(request, 'interfaceBDD/home.html', {'allQuestions': questions})


def addition(request, nombre1, nombre2):    
    total = int(nombre1) + int(nombre2)
    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'interfaceBDD/addition.html', locals())
    
def proposition(request):
    
    propQuestion = PropositionForm(request.POST or None)
    
    if propQuestion.is_valid():
        propQuestion.save()
        
    return render(request, 'interfaceBDD/propositionQuestion.html', locals())
        