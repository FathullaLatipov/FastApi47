from database.models import User, UserAnswers, Questions, Result
from datetime import datetime

from database import get_db


# регистрация
def register_user_db(name, phone_number, level):
    db = next(get_db())
    checker = db.query(User).filter_by(phone_number=phone_number).first()
    if checker:
        return checker.id
    else:
        new_user = User(name=name, phone_number=phone_number,
                        level=level, created_at=datetime.now())
        db.add(new_user)
        db.commit()
        return new_user.id


# Получить всех пользователей
def get_all_users_db():
    db = next(get_db())
    all_users = db.query(User).all()
    return all_users


# Ответы пользователя
def user_answer_db(user_id, q_id, level, user_answer):
    db = next(get_db())
    exact_question = db.query(Questions).filter_by(id=q_id).first()
    if exact_question:
        if exact_question.correct_answer == user_answer:
            correctness = True
        else:
            correctness = False

        # создаем новый обьект
        new_answer = UserAnswers(user_id=user_id,
                                 q_id=q_id,
                                 user_answer=user_answer,
                                 level=level,
                                 correctness=correctness)
        db.add(new_answer)
        db.commit()
        return True if correctness else False
    else:
        return 'Вопрос не найден'
