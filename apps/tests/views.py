from django.shortcuts import render

from .models import Test

from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def test(request):
    all_tests = Test.objects.all()
    context = {
        'all_tests': all_tests
    }
    return render(request, 'tests/test.html', context)
