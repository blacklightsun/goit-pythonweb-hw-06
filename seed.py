from models import Score, Student, Subject, Teacher, Group
from faker import Faker

from connect import session

def seed_data(session):

    faker = Faker()

    # Create Teachers
    teachers = []

    for _ in range(5):
        teachers.append(Teacher(name=faker.name()))

    session.add_all(teachers)
    session.commit()
    print("Teachers seeded successfully.")

    # Create Subjects
    subjects = [
        Subject(name="Mathematics", teacher_id=teachers[0].id),
        Subject(name="History", teacher_id=teachers[1].id),
        Subject(name="Science", teacher_id=teachers[2].id),
        Subject(name="Literature", teacher_id=teachers[0].id),
        Subject(name="Art", teacher_id=teachers[1].id),
        Subject(name="Physical Education", teacher_id=teachers[2].id),
        Subject(name="Biology", teacher_id=teachers[3].id),
        Subject(name="Chemistry", teacher_id=teachers[4].id),
    ]

    # for _ in range(8):
    #     subjects.append(Subject(name=faker.word().capitalize(), teacher_id=faker.random_element(teachers).id))

    session.add_all(subjects)
    session.commit()
    print("Subjects seeded successfully.")

    # Create Groups
    groups = [
        Group(name="Group A"),
        Group(name="Group B"),
        Group(name="Group C"),
    ]
    session.add_all(groups)
    session.commit()
    print("Groups seeded successfully.")

    # Create Students
    students = []

    for _ in range(50):
        students.append(Student(name=faker.name(), group_id=faker.random_element(groups).id))
    session.add_all(students)
    session.commit()
    print("Students seeded successfully.")

    # Create Scores
    scores = []

    for student in students:
        for subject in faker.random_elements(subjects, length=5, unique=True):
            scores.append(Score(student_id=student.id, subject_id=subject.id, score=faker.random_int(min=60, max=100), created=faker.date_between(start_date='-3M', end_date='today')))
    session.add_all(scores)
    session.commit()
    print("Scores seeded successfully.")

seed_data(session)
print("Database seeded successfully.")