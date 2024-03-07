from .models import Questions, Result
from database import get_db


# Топ 5 лидеров
def get_5_leaders_db():
    db = next(get_db())
    leaders = db.query(Result.user_id).order_by(Result.correct_answers.desc())
    return leaders[:5]


# Мы сами добавляем вопросы и вырианты и ответ к вопросу
def add_question_db(q_text, v1, v2, v3, v4, correct_answer):
    db = next(get_db())
    new_question = Questions(q_text=q_text, v1=v1, v2=v2, v3=v3, v4=v4,
                             correct_answer=correct_answer)
    db.add(new_question)
    db.commit()
    return 'Вопрос успешно добавлен!'


# Получить только 20 вопросов
def get_questions_db():
    db = next(get_db())

    questions = db.query(Questions).all()

    return questions[:20]
