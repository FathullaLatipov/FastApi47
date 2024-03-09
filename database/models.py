from sqlalchemy import Column, DateTime, String, Boolean, ForeignKey, Time, Integer
from sqlalchemy.orm import relationship

from database import Base


# Таблица пользователей
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    phone_number = Column(Integer, unique=True)
    level = Column(String, default='None')
    created_at = Column(DateTime)


# Таблица вопросов
class Questions(Base):
    __tablename__ = 'questions'
    id = Column(Integer, autoincrement=True, primary_key=True) #4
    q_text = Column(String) # Что такое Питон?
    v1 = Column(String) # This is snake
    v2 = Column(String) # This is python language
    v3 = Column(String) # This is bla
    v4 = Column(String) # this is Hello
    correct_answer = Column(Integer, nullable=False) #2
    timer = Column(Time)
    created_at = Column(DateTime)


# Таблица результатов и для лидеров
class Result(Base):
    __tablename__ = 'results'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))  # 3
    correct_answers = Column(Integer, default=0)
    level = Column(String)
    # Если выйдет ошибка то исправим
    user_fk = relationship(User, lazy='subquery')


# Ответы пользователя на вопросы)))
class UserAnswers(Base):
    __tablename__ = 'user_answers'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    q_id = Column(Integer, ForeignKey('questions.id'))
    level = Column(String, ForeignKey('users.level'))
    user_answer = Column(Integer)
    correctness = Column(Boolean, default=False)
    timer = Column(Time)

    # Если выйдет ошибка то исправим
    user_fk = relationship(User, foreign_keys=[user_id], lazy='subquery')
    question_fk = relationship(Questions, foreign_keys=[q_id], lazy='subquery')
