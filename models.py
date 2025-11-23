from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.sql import func
from datetime import datetime


class Base(DeclarativeBase):
    pass


class Student(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"), nullable=False)

    group: Mapped["Group"] = relationship()

    def __repr__(self) -> str:
        return f"Student(id={self.id}, name='{self.name}', group_id={self.group_id})"


class Teacher(Base):
    __tablename__ = "teachers"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return f"Teacher(id={self.id}, name='{self.name}')"


class Group(Base):
    __tablename__ = "groups"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return f"Group(id={self.id}, name='{self.name}')"


class Subject(Base):
    __tablename__ = "subjects"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    teacher_id: Mapped[int] = mapped_column(ForeignKey("teachers.id"), nullable=False)
    
    teacher: Mapped["Teacher"] = relationship()

    def __repr__(self) -> str:
        return f"Subject(id={self.id}, name='{self.name}', teacher_id={self.teacher_id})"


class Score(Base):
    __tablename__ = "scores"
    id: Mapped[int] = mapped_column(primary_key=True)
    created: Mapped[datetime] = mapped_column(default=func.now())
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"), nullable=False)
    subject_id: Mapped[int] = mapped_column(ForeignKey("subjects.id"), nullable=False)
    score: Mapped[int] = mapped_column(nullable=False)

    student: Mapped["Student"] = relationship()
    subject: Mapped["Subject"] = relationship()

    def __repr__(self) -> str:
        return (f"Score(id={self.id}, created={self.created}, student_id={self.student_id}, "
                f"subject_id={self.subject_id}, score={self.score})")
    
