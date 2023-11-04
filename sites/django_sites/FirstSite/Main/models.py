from django.db.models import *


class Position(Model):
    name = CharField(max_length=40, null=True, blank=True)
    description = TextField(max_length=500)
    min_expirience = IntegerField()

    def __str__(self):
        return f"{self.name}"


class Skill(Model):
    name = CharField(max_length=40)

    def __str__(self):
        return f"{self.name}"


class Candidate(Model):
    surname = CharField(max_length=40)
    age = IntegerField(default=20)
    test_task_mark = IntegerField(null=True, blank=True)
    interview_mark = IntegerField(null=True, blank=True)
    salary_exp = IntegerField(null=True, blank=True)
    position = ForeignKey(Position, on_delete=PROTECT, related_name="candidates")
    skills = ManyToManyField(Skill, related_name="candidates")

    def __str__(self):
        return f"{self.surname} ({self.age})"
