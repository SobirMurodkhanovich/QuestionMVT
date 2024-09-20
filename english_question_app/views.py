from django.shortcuts import render, redirect
from .models import Question, Answer
from django.http import HttpResponse


def question_view(request):
    selected_level = request.GET.get('level', 'beginner')
    questions = Question.objects.filter(level=selected_level)
    return render(request, 'questions.html',
                  {'questions': questions, 'selected_level': selected_level})


def submit_answers(request):
    if request.method == 'POST':
        score = 0
        total = Question.objects.count()
        for question in Question.objects.all():
            selected_answer_id = request.POST.get(f'question_{question.id}')
            if selected_answer_id:
                selected_answer = Answer.objects.get(id=selected_answer_id)
                if selected_answer.is_correct:
                    score += 1

        percentage = (score / 50) * 100 if total > 0 else 0
        return render(request, 'results.html',
                      {'score': score, 'total': total, 'percentage': percentage})

    return redirect('question_view')
