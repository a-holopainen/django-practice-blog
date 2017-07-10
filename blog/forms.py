from django import forms

from .models import Problem


class ProblemForm(forms.ModelForm):

    class Meta:
        model = Problem
        fields = ('title', 'text', 'status', 'start_type', 'end_type', 'grade', 'grip_color', 'problem_img')
