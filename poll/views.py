from django.shortcuts import get_object_or_404, render
from .models import Choice, Question

def list(request):
    list = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'poll/poll_list.html', {'latest_question_list':list})

def detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    choice_set = Choice.objects.filter(question=pk)
    return render(request, 'poll/poll_detail.html', {'question':question, 'choice_set':choice_set})

def result(request, pk):
    question = get_object_or_404(Question, pk=pk)
    choice_set = Choice.objects.filter(question=pk)
    return render(request, 'poll/poll_results.html', {'question':question, 'choice_set':choice_set})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = Choice.objects.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'poll/poll_detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return result(request, question_id)

