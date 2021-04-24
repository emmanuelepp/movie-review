from fastapi import FastAPI
from database import database as conn
from database import User
from database import Movie
from database import UserReview

app = FastAPI(title='Hello')


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
