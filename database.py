from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine('sqlite:///contatos.db', echo=True, connect_args={'check_same_thread': False})

Base = declarative_base()

class User(Base): 
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    contatos = relationship('Contato', back_populates='user')


class Contato(Base):
    __tablename__ = 'contatos'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    telefone = Column(String(15), nullable=False)
    tags = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='contatos')


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()