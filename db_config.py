from peewee import Database, MySQLDatabase

database = MySQLDatabase('DATABASE', user='',
                         password='',
                         host='',
                         port='')


class User(Model):
    userName = CharField(max_length=60, unique=True)
    password = CharField(max_length=60)
    create_date = DateField(default=datetime.now)

    def __str__(self):
        return self.userName

    class Meta:
        database = database
        table_name = 'users'


class Movie(Model):
    title = CharField(max_length=60)
    create_date = DateTimeField(datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        database = database
        table_name = 'movies'


class UserReview(Model):
    user = ForeignKeyField(User, backref='reviews')
    movie = ForeignKeyField(Movie, backref='reviews')
    reviews = TextField()
    score = IntegerField()
    create_date = DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.username} - {self.movie.title}'

    class Meta:
        database = database
        table_name = 'user_reviews'
