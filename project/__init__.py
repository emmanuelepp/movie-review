from fastapi import FastAPI

from .routers import user_router
from .routers import review_router

from .database import database as conn
from .database import User
from .database import Movie
from .database import UserReview


app = FastAPI(title='Movie review API')
app.include_router(user_router)
app.include_router(review_router)


@app.on_event('startup')
def startup():
    if conn.is_closed():
        conn.connect()

    conn.create_tables([User, Movie, UserReview])


@app.on_event('shutdown')
def shutdown():
    if not conn.is_closed():
        conn.close()
