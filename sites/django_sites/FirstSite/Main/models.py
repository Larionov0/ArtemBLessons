from django.db.models import *


class Candidate(Model):
    surname = CharField(max_length=40)
    age = IntegerField(default=20)
    test_task_mark = IntegerField(null=True, blank=True)
    interview_mark = IntegerField(null=True, blank=True)
    salary_exp = IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.surname} ({self.age})"
