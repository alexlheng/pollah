from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
#from django.template import loader #not needed if using render

from .models import pollah_question

# Create your views here.

def index(request):
    recent_questions = pollah_question.objects.order_by('-time_created')[:5]
    #output = ', '.join([p.question_text for p in recent_questions])
    context = {'recent_questions':recent_questions}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("This is question %s." % question_id)

def results(request, question_id):
    response = "These are the answers to question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Please vote on question %s." % question_id)

def details(request, question_id):
	question = get_object_or_404(pollah_question, pk=question_id)
	return render(request, 'polls/detail.html', {'pollah_question': pollah_question})