from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режиссер', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Тарантино'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Чикаго'),
    'description': fields.String(required=True, max_length=255, example='Рокси Харт мечтает о песнях и танцах и о '
                                                                        'том, как сравняться с самой Велмой Келли, '
                                                                        'примадонной водевиля. И Рокси действительно '
                                                                        'оказывается с Велмой в одном положении, '
                                                                        'когда несколько очень неправильных шагов '
                                                                        'приводят обеих на скамью подсудимых.'),
    'trailer': fields.String(required=True, max_length=100, example='https://www.youtube.com/watch?v=YxzS_LzWdG8'),
    'year': fields.String(required=True, max_length=100, example='2002'),
    'rating': fields.String(required=True, max_length=100, example='7.2'),
    'genre': fields.Nested(genre),
    'director': fields.Nested(director)
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=100, example='olya@mail.ru'),
    'password': fields.String(required=True, max_length=100, example='060793'),
    'name': fields.String(required=True, max_length=100, example='Olya'),
    'surname': fields.String(required=True, max_length=100, example='Petrushina'),
    'genre': fields.Nested(genre)
})
