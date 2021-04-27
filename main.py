from fastapi import FastAPI
from fastapi import HTTPException
from database import database as conn

from database import User
from database import Movie
from database import UserReview

from schemas import UserRequestModel
from schemas import UserResponseModel
from schemas import ReviewRequestModel
from schemas import ReviewResponseModel


app = FastAPI(title='Movie review API')


@app.get('/')
async def index():
    return ''


@app.get('/about')
async def about():
    return ''


@app.on_event('startup')
def startup():
    if conn.is_closed():
        conn.connect()

    conn.create_tables([User, Movie, UserReview])


@app.on_event('shutdown')
def shutdown():
    if not conn.is_closed():
        conn.close()


@app.post('/users', response_model=UserResponseModel)
async def create_user(user: UserRequestModel):

    if User.select().where(User.username == user.username).exists():

        return HTTPException(409, 'User name already exist.')

    hash_pssword = User.encrypt_password(user.password)

    user = User.create(
        username=user.username,
        password=hash_pssword
    )

    return user


@app.post('/reviews', response_model=ReviewResponseModel)
async def create_reviews(user_review: ReviewRequestModel):

    user_review = UserReview.create(

        user_id=user_review.user_id,
        movie_id=user_review.movie_id,
        reviews=user_review.review,
        score=user_review.score
    )

    return user_review
