from sqlalchemy import func

from models import Score, Student, Subject, Teacher, Group
from connect import session

print()
print("1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.")
results = session.query(Score).join(Student) \
    .with_entities(Student.name.label('student_name'),
    func.avg(Score.score).label('avg_score')) \
    .group_by(Student.name) \
    .order_by(func.avg(Score.score).desc()) \
    .limit(5).all()

for res in results:
    print(res)


print()
print("2. Знайти студента із найвищим середнім балом з певного предмета.")
results = session.query(Score).join(Student).join(Subject) \
    .with_entities(Student.name.label('student_name'),
    func.avg(Score.score).label('avg_score')) \
    .filter(Subject.name == 'Art') \
    .group_by(Student.name) \
    .order_by(func.avg(Score.score).desc()) \
    .limit(1).all()

for res in results:
    print(res)


print()
print("3. Знайти середній бал у групах з певного предмета.")
results = session.query(Score).join(Student).join(Subject).join(Group) \
    .with_entities(Group.name.label('group_name'),
    func.avg(Score.score).label('avg_score')) \
    .filter(Subject.name == 'Science') \
    .group_by(Group.name) \
    .order_by(func.avg(Score.score).desc()) \
    .all()

for res in results:
    print(res)


print()
print("4. Знайти середній бал на потоці (по всій таблиці оцінок).")
results = session.query(Score).join(Student).join(Group) \
    .with_entities(Group.name.label('group_name'),
    func.avg(Score.score).label('avg_score')) \
    .group_by(Group.name) \
    .order_by(func.avg(Score.score).desc()) \
    .all()

for res in results:
    print(res)


print()
print("5. Знайти які курси читає певний викладач.")
results = session.query(Subject).join(Teacher) \
    .with_entities(Subject.name.label('subject_name')) \
    .filter(Teacher.name == 'Kristi Ford') \
    .all()

for res in results:
    print(res)


print()
print("6. Знайти список студентів у певній групі.")
results = session.query(Student).join(Group) \
    .with_entities(Student.name.label('student_name')) \
    .filter(Group.name == 'Group A') \
    .all()

for res in results:
    print(res)


print()
print("7. Знайти оцінки студентів у окремій групі з певного предмета.")
results = session.query(Score).join(Student).join(Subject).join(Group) \
    .with_entities(Student.name.label('student_name'),
    Score.score.label('score')) \
    .filter(Subject.name == 'Mathematics', Group.name == 'Group B') \
    .order_by(Score.score.desc()) \
    .all()

for res in results:
    print(res)


print()
print("8. Знайти середній бал, який ставить певний викладач зі своїх предметів.")
results = session.query(Score).join(Subject).join(Teacher) \
    .with_entities(func.avg(Score.score).label('average_score')) \
    .filter(Teacher.name == 'Kristi Ford') \
    .all()

for res in results:
    print(res)


print()
print("9. Знайти список курсів, які відвідує певний студент.")
results = session.query(Score).join(Student).join(Subject) \
    .with_entities(Subject.name.label('subject_name')) \
    .filter(Student.name == 'Nathan Johnson') \
    .distinct() \
    .all()

for res in results:
    print(res)


print()
print("10. Список курсів, які певному студенту читає певний викладач.")
results = session.query(Score).join(Student).join(Subject).join(Teacher) \
    .with_entities(Subject.name.label('subject_name')) \
    .filter(Student.name == 'Nathan Johnson', Teacher.name == 'Kristi Ford') \
    .distinct() \
    .all()

for res in results:
    print(res)


print()
print("11. Середній бал, який певний викладач ставить певному студентові.")
results = session.query(Score).join(Student).join(Subject).join(Teacher) \
    .with_entities(func.avg(Score.score).label('average_score')) \
    .filter(Teacher.name == 'Kristi Ford', Student.name == 'Nathan Johnson') \
    .all()

for res in results:
    print(res)


print()
print("12. Оцінки студентів у певній групі з певного предмета на останньому занятті.")
denorm_table = session.query(Score).join(Student).join(Subject).join(Group) \
    .with_entities(Student.name.label('student_name'),
    Score.score.label('score'),
    Score.created.label('created')) \
    .filter(Subject.name == 'Art', Group.name == 'Group B') \
    .cte("denorm_table") 

results = session.query(denorm_table) \
    .with_entities(denorm_table.c.student_name,
    denorm_table.c.score) \
    .filter(denorm_table.c.created == session.query(func.max(denorm_table.c.created)).scalar_subquery()) \
    .all()

for res in results:
    print(res)


session.close()