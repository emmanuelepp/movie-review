from fastapi import FastAPI
from fastapi import HTTPException
from database import database as conn
from database import User
from database import Movie
from database import UserReview
from schemas import UserBaseModel


app = FastAPI(title='Movie review API')


@app.get('/')
async def index():
    return 'Hello'


@app.get('/about')
async def about():
    return 'Hello'


@app.on_event('startup')
def startup():
    if conn.is_closed():
        conn.connect()

    conn.create_tables([User, Movie, UserReview])


@app.on_event('shutdown')
def shutdown():
    if not conn.is_closed():
        conn.close()


@app.post('/users')
async def create_user(user: UserBaseModel):

    if User.select().where(User.username == user.username).exists():

        return HTTPException(409, 'User name already exist.')

    hash_pssword = User.encrypt_password(user.password)

    user = User.create(
        username=user.username,
        password=hash_pssword
    )

    return user.id
