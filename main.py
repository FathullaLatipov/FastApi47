from fastapi import FastAPI

app = FastAPI(docs_url='/')


# uvicorn main:app --reload
@app.get("/")
async def home():
    return {"Hello": "World"}


@app.get('/users', tags=['This method for users'], description='This method for get all users')
async def users():
    return {'User': 'John'}


@app.post('/products', tags=['This method for products'])
async def users(title: str, price: int, description: str):
    return {'product': f'Название: {title} цена: {price}$ описания {description}'}


@app.get('/param-example')
async def param(user_id: int, user_answer: str):
    return {'message': f'У этого пользователя {user_id} примерно 10 ответов и этот ответ {user_answer}'}


@app.put('/products', tags=['This method for products'])
async def product_change(title: str, price: int, description: str):
    return {'Update info': f'Новые данные {title} новая цена {price} новая описания {description}'}


@app.delete('/products', tags=['This method for products'])
async def product_delete(title: str):
    return {'Ответ': f'Этот продукт {title} удален из базы!'}

# Параметры для запроса

