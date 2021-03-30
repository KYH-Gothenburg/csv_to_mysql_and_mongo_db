from data.db import Base
import sqlalchemy as sa
from sqlalchemy.orm import relationship
from .movies import Movie
from .characters import Character


class Conversation(Base):
    __tablename__ = 'conversations'

    conversations_id = sa.Column(sa.Integer, primary_key=True)
    characters_character1_id = sa.Column(sa.String(6), sa.ForeignKey('characters.character_id'), nullable=False)
    characters_character2_id = sa.Column(sa.String(6), sa.ForeignKey('characters.character_id'), nullable=False)
    movies_movie_id = sa.Column(sa.String(5), sa.ForeignKey('movies.movie_id'), nullable=False)

    conversation_lines = relationship('ConversationLine', order_by="ConversationLine.conversation_line_pos")


class ConversationLine(Base):
    __tablename__ = 'conversation_lines'

    conversation_line_id = sa.Column(sa.Integer, primary_key=True)
    conversation_line_pos = sa.Column(sa.Integer, nullable=False)
    conversations_conversations_id = sa.Column(sa.Integer, sa.ForeignKey('conversations.conversations_id'), nullable=False)
    movie_lines_line_id = sa.Column(sa.String(10), sa.ForeignKey('movie_lines.line_id'), nullable=False)

    text_line = relationship('MovieLine')

class MovieLine(Base):
    __tablename__ = 'movie_lines'

    line_id = sa.Column(sa.String(10), primary_key=True)
    line_text = sa.Column(sa.Text, nullable=False)
    characters_character_id = sa.Column(sa.String(6), sa.ForeignKey('characters.character_id'), nullable=False)
    movies_movie_id = sa.Column(sa.String(5), sa.ForeignKey('movies.movie_id'), nullable=False)