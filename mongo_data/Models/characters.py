import sqlalchemy as sa
from sql_data.db import Base
from .movies import Movie


class Character(Base):
    __tablename__ = 'characters'

    character_id = sa.Column(sa.String(6), primary_key=True)
    character_name = sa.Column(sa.String(150), nullable=False)
    gender = sa.Column(sa.String(5), nullable=True)
    movies_movie_id = sa.Column(sa.String(5), sa.ForeignKey('movies.movie_id'), nullable=False)




    def __repr__(self):
        return f'{self.movie_title} - {self.movie_year}'