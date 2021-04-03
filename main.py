from fastapi import FastAPI

app = FastAPI(title='Hello')


@app.get('/')
async def index():
    return 'Hello'


@app.get('/about')
async def about():
    return 'Hello'


@app.on_event('startup')
def startup():
    return 'Server start'


@app.on_event('shutdown')
def shutdown():
    return 'Server start'
