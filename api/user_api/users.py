from fastapi import APIRouter
from database.userservice import register_user_db, user_answer_db, \
    plus_point_user_db, get_all_users_db
from database.testservice import get_questions_db, add_question_db

# 15
user_router = APIRouter(prefix='/user', tags=['Работа с пользователями'])


# Регистарция пользователя на SWAGGER UI
@user_router.post('/register')
async def register(name: str, phone_number: int, level: str):
    register_user = register_user_db(name, phone_number, level)
    print(name, phone_number, level)
    return f'Вы успешно прошли регистрацию {register_user}'


@user_router.get('/all_users')
async def all_users():
    return get_all_users_db()


@user_router.get('/leaders')
async def get_leaders(user_id: int, q_id: int, level: str, user_answer: int):
    get_leader = user_answer_db(user_id, q_id, level, user_answer)
    return f'Лидеры {get_leader}'


@user_router.post('/plus')
async def plus_point(user_id: int, correct_answers: int):
    done = plus_point_user_db(user_id, correct_answers)
    return f'Результат {done}'
