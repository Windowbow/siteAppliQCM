from datetime import datetime
from django.shortcuts import render
from .models import Question, PropQuestion
from .forms import PropositionForm

class VerifQuestion(ListView):
    model = PropQuestion
    context_object_name = "lattestSubmittedQuestion"
    template_name = 'interfaceBDD/verifieQuestion.html'
    paginate_by = 5

def date_actuelle(request):
    return render(request, 'interfaceBDD/date.html', {'date': datetime.now()})

def home(request):
    return render(request, 'interfaceBDD/home.html', {})

def validation(request):
    tests = Question.objects.all()
    return render(request, 'interfaceBDD/verifieQuestion.html', {'allTests': tests})

def addition(request, nombre1, nombre2):    
    total = int(nombre1) + int(nombre2)
    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'interfaceBDD/addition.html', locals())
    
def proposition(request):
    
    propQuestion = PropositionForm(request.POST or None)
    
    if propQuestion.is_valid():
        propQuestion.save()
        
    return render(request, 'interfaceBDD/propositionQuestion.html', locals())
        