from django.shortcuts import render, get_object_or_404, redirect

from .models import Test, Registration
from .forms import CreateTestForm

from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required
def test(request):
    all_tests = Test.objects.all()
    context = {
        'all_tests': all_tests,
        'created_form': CreateTestForm
    }
    return render(request, 'tests/test.html', context)

@login_required
def create_test(request):
    if request.method == 'POST':
        form = CreateTestForm(request.POST)
        if form.is_valid():
            test = form.save(commit=False)
            test.author = request.user
            test.save()
            messages.success(request, 'Автор опублікував новий тест')
            return redirect('tests:test')
        else:
            messages.error(request, f'У {test.author} не вийшло опублікувати тест')
    else:
        form = CreateTestForm()
        
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
    registration = Registration.objects.create(test=test, user=request.user)
    if request.method == 'POST':
        if registration:
            messages.success(request, 'Вітаю з успішною реєстрацією на тест')
            return redirect('tests:test')
        else:
            messages.error(request, 'У вас не вийшло зареєструватися на тест')

    return render(request, 'tests/registration_test.html', {'registration': registration, 'test': test})
