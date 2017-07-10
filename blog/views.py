from django.utils import timezone
from .models import Problem
from django.shortcuts import render, get_object_or_404
from .forms import ProblemForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    problems = Problem.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/index.html', {'problems': problems})


def problem_detail(request, pk):
    problem = get_object_or_404(Problem, pk=pk)
    return render(request, 'blog/problem_detail.html', {'problem': problem})


@login_required
def problem_new(request):
    if request.method == "POST":
        form = ProblemForm(request.POST, request.FILES)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.builder = request.user
            problem.save()
            return redirect('problem_detail', pk=problem.pk)
    else:
        form = ProblemForm()
    return render(request, 'blog/problem_edit.html', {'form': form})


@login_required
def problem_edit(request, pk):
    problem = get_object_or_404(Problem, pk=pk)
    if request.method == "POST":
        form = ProblemForm(request.POST, instance=problem)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.builder = request.user
            problem.save()
            return redirect('problem_detail', pk=problem.pk)
    else:
        form = ProblemForm(instance=problem)
    return render(request, 'blog/problem_edit.html', {'form': form})


@login_required
def problem_draft_list(request):
    problems = Problem.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/problem_draft_list.html', {'problems': problems})


@login_required
def problem_publish(request, pk):
    problem = get_object_or_404(Problem, pk=pk)
    problem.publish()
    return redirect('problem_detail', pk=pk)


@login_required
def problem_remove(request, pk):
    problem = get_object_or_404(Problem, pk=pk)
    problem.delete()
    return redirect('post_list')