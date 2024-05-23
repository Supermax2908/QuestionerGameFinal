from django.shortcuts import render, get_object_or_404, redirect

from .models import Test, Question
from .forms import TestForm, QuestionForm

from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required
def test(request):
    all_tests = Test.objects.all()
    context = {
        'all_tests': all_tests,
        'created_form': TestForm
    }
    return render(request, 'tests/test.html', context)

@login_required
def create_test(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            test = form.save(commit=False)
            test.author = request.user
            test.save()
            messages.success(request, 'Автор опублікував новий тест')
            return redirect('tests:test')
        else:
            messages.error(request, f'У {test.author} не вийшло опублікувати тест')
    else:
        form = TestForm()
        
@login_required
def delete_test(request, test_id):
    if request.method == 'POST':
        test = get_object_or_404(Test, pk=test_id, author=request.user)
        test.delete()
        messages.success(request, 'Post deleted succesfuly')
        return redirect('tests:test')
    else:
        messages.error(request, 'Error updating post')
    return redirect('introduction:welcome')

@login_required
def registration_test(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    
    if request.method == 'POST':
        if test.author == request.user:
            return redirect('tests:create_question')
        elif test.author != request.user:
            questions = Question.objects.filter(test=test)
            if questions:
                first_question = questions.first()
                messages.success(request, 'Починаємо!')
                return redirect('tests:question', slug=first_question.slug)
            else:
                messages.error(request, 'Для цього тесту немає доступних питань.')
    return render(request, 'tests/registration_test.html', {'test': test})

@login_required
def take_question(request, slug):
    question = get_object_or_404(Question, slug=slug)
    return render(request, 'tests/question.html', {'question': question})

@login_required
def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            messages.success(request, 'Питання успішно створено!')
        else:
            messages.error(request, 'Помилка! Питання не було створено.')
    else:
        form = QuestionForm()
    return render(request, 'tests/question.html', {'question_form': form})

@login_required
def delete_question(request, slug):
    question = get_object_or_404(Question, slug=slug)
    if request.method == 'POST':
        question.delete()
        messages.success(request, 'Запитання успішно видалено.')
        return redirect('tests:question')
    return render(request, 'tests/delete_question.html', {'question': question})

