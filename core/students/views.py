import datetime
from django.shortcuts import render
from django.db.models import Q, F, Max, Min, OuterRef, Subquery, Count
from .models import Student, Teacher


def student_list(request):
    posts = Student.objects.all()
    print(posts)
    return render(request, 'output.html', {'posts': posts})

def student_OR_filter(request):
    post = Student.objects.filter(Q(surname__startswith='astin') | Q(surname__startswith='baldwin') | ~Q(surname__startswith='parker'))

def student_And_filter(request):
    post = Student.objects.exclude(classroom=3) & Student.objects.filter(firstname__startswith='alaska')

def student_Union_list(request):
    post = Student.objects.all().values_list("firstname").union(Teacher.objects.all().values_list("firstname"))

def update_student(request):
    b = Student(age='19', surname='babal')
    b.save()

def update_foreign_key(request):
    student = Student.objects.get(pk=1)
    teacher = Teacher.objects.get(name='Tika ram')
    student.teacher = teacher
    student.save()

def update_many_to_many(request):
    student = Student.objects.get(id=1)
    new_student = Student.objects.create(firstname='student 1')
    student.teachers.add(new_student)

def retrieve_by_year(request):
    student = Student.objects.filter(joined_date__year=2001)

def chaining_filter(request):
    student = Student.objects.filter(joined_date__year=2001).exclude(firstname__startswith='naami').filter(joined_date__gte=datetime.date(2005, 1, 3))

    student = Student.objects.filter(student__surname__contains="babal").filter(student__joined_date__year=2002)

def F_expression(request):
    student = Student.objects.filter(joined_date__gt=F("update_date"))
    student = Student.objects.filter(joined_date__gt=F("update_date") + datetime.timedelta(days=3))

def aggregate(request):
    student = Student.objects.aggregate(last_joined_year=Max("joined_date__year"))
    student = Student.objects.aggregate(last_joined_year=Min("joined_date__year"))

def annotate(request):
    student = Student.objects.values("joined_date__year").annotate(
        top_year=Subquery(Student.objects.filter(joined_date__year=OuterRef("joined_date__year"),).order_by("-rating")),
        total_student=Count("id")
        )
    
def extract_field(request):
    student_name = Student.objects.filter(id=1).only("firstname", "surname")