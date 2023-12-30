# myapp/scripts/create_initial_data.py
import random
from faker import Faker
from django.contrib.auth.models import User
from record.models import Professor, Course, Student, Enrollment, Assignment, Grade
from django.utils import timezone
from django.core.management.base import BaseCommand

fake = Faker()

class Command(BaseCommand):
    help = 'Create initial data for the myapp models'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Creating initial data...'))

        # Create professors
        professors = []
        for _ in range(10):
            professor = Professor(
                FirstName=fake.first_name(),
                LastName=fake.last_name(),
                Email=fake.email(),
                Department=fake.word()
            )
            professor.save()
            professors.append(professor)

        # Create courses with professors
        courses = []
        for _ in range(10):
            course = Course(
                CourseName=fake.word(),
                Department=fake.word(),
                ProfessorID=random.choice(professors)
            )
            course.save()
            courses.append(course)

        # Create students
        students = []
        for _ in range(20):
            student = Student(
                FirstName=fake.first_name(),
                LastName=fake.last_name(),
                Email=fake.email()
            )
            student.save()
            students.append(student)

        # Enroll students in courses
        for course in courses:
            for _ in range(random.randint(5, 15)):
                student = random.choice(students)
                Enrollment.objects.create(StudentID=student, CourseID=course)

        # Create assignments for courses
        assignments = []
        for course in courses:
            for _ in range(random.randint(2, 5)):
                assignment = Assignment(
                    AssignmentName=fake.word(),
                    Deadline=timezone.now() + timezone.timedelta(days=random.randint(5, 30)),
                    CourseID=course
                )
                assignment.save()
                assignments.append(assignment)

        # Assign grades to students for assignments
        for assignment in assignments:
            for enrollment in Enrollment.objects.filter(CourseID=assignment.CourseID):
                Grade.objects.create(StudentID=enrollment.StudentID, AssignmentID=assignment, Score=random.uniform(60, 100))

        self.stdout.write(self.style.SUCCESS('Initial data created successfully.'))
