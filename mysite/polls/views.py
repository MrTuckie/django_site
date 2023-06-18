from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import Question

# Create your views here.


# você precisa vincular essa função a uma página (url)
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5] # ordenando as 5 mais recentes
    context = {'latest_question_list':latest_question_list} # é o que vai aparecer na página
    return render(request, 'polls/index.html',context) # ele cria a página


def results(request,question_id):
    question = Question(pk=question_id) # primary_key (é o id da pergunta)
    return render(request, 'polls/results.html',{'question':question})

def vote( request, question_id):
    question = get_object_or_404(Question, pk=question_id) # essa questão existe ou não?
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) # vai postar o voto no banco de dados
    except KeyError:
        return render(request, 'polls/vote.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save() # registrando as informações
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,))) #redirecionando a página de resultados