from fastapi import APIRouter
from database.userservice import user_answer_db
from database.testservice import get_questions_db, add_question_db

test_router = APIRouter(prefix='/test', tags=['Работа с тестами'])


# Получить все 20 вопросов
@test_router.get('/all-tests')
async def all_20_questions():
    return get_questions_db()


# Для добавлении вопросов
@test_router.post('/add-question')
async def add_question(q_text: str, v1: str, v2: str, v3: str, v4: str, correct_answer: int):
    new_q = add_question_db(q_text, v1, v2, v3, v4, correct_answer)
    return f'Успешно добавлен {new_q}'


# Получить ответы пользователя
@test_router.get('/user-answers')
async def get_user_answer(user_id: int, q_id: int, level: str, user_answer: int):
    u_answer = user_answer_db(user_id, q_id, level, user_answer)
    return f'Успешно и вот данные {u_answer}'
