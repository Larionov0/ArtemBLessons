from django.shortcuts import render
from .models import *


def candidates(request):
    candidates_data = Candidate.objects.all()

    return render(request, 'candidates.html', context={
        'amount': len(candidates_data),
        'headers': ['Surname', 'Age', 'TestTask', 'Inteview', 'Salary'],
        'candidates_data': candidates_data,
    })
