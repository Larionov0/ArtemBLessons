from django.http import HttpResponse


candidates_data = [
    {
        'surname': 'Anlov',
        'age': 19,
        'test_task_mark': 89,
        'interview_mark': 60,
        'salary_exp': 2000
    },
    {
        'surname': 'Bobenko',
        'age': 56,
        'test_task_mark': 98,
        'interview_mark': 89,
        'salary_exp': 5000
    },
    {
        'surname': 'Vasilenko',
        'age': 34,
        'test_task_mark': 78,
        'interview_mark': 67,
        'salary_exp': 3000
    },
    {
        'surname': 'Golovach',
        'age': 23,
        'test_task_mark': 90,
        'interview_mark': 80,
        'salary_exp': 4000
    },
    {
        'surname': 'Dobro',
        'age': 45,
        'test_task_mark': 85,
        'interview_mark': 75,
        'salary_exp': 3500
    },
    {
        'surname': 'Egorenko',
        'age': 32,
        'test_task_mark': 99,
        'interview_mark': 90,
        'salary_exp': 6000
    },
    {
        'surname': 'Zakhar',
        'age': 28,
        'test_task_mark': 67,
        'interview_mark': 55,
        'salary_exp': 2000
    },
]


def test_lol(request):
    return HttpResponse('<h1>LOL page</h1><p>This is my first test page</p>')


def candidates(request):
    html = '<table>'
    headers = ['Surname', 'Age', 'TestTask', 'Inteview', 'Salary']

    html += '<tr>'
    for header in headers:
        html += f'<td>{header}</td>'
    html += '</tr>'

    for candidate in candidates_data:
        html += f'<tr><td>{candidate["surname"]}</td><td>{candidate["age"]}</td><td>{candidate["test_task_mark"]}</td><td>{candidate["interview_mark"]}</td><td>{candidate["salary_exp"]}</td></td>'
    html += '</table>'

    return HttpResponse(html)
