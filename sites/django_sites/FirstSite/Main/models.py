from django.db.models import *


class Candidate(Model):
    surname = CharField(max_length=40)
    age = IntegerField(default=20)
    test_task_mark = IntegerField()
    interview_mark = IntegerField()
    salary_exp = IntegerField()
