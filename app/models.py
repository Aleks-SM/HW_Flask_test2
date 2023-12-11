import os
import datetime
import sqlalchemy as sq
from sqlalchemy import String, DateTime, func, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Mapped, mapped_column



POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "secret")
POSTGRES_USER = os.getenv("POSTGRES_USER", "app")
POSTGRES_DB = os.getenv("POSTGRES_DB", "app")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5431")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "127.0.0.1")

PG_DSN = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_engine(PG_DSN)
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass


#Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True)
    registration_time: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=func.now())
    # id = sq.Column(sq.Integer, primary_key=True)
    # name = sq.Column(sq.String(length=40), unique=True, nullable=False)
    # password = sq.Column(sq.String(70), nullable=False)
    # email = sq.Column(sq.String(length=40), index=True, unique=True)

    @property
    def dict(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'registration_time': self.registration_time.isoformat()
        }

class Advertisement(Base):
    __tablename__ = "advertisement"

    adv_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(20), nullable=False)
    description: Mapped[str] = mapped_column(String(240), nullable=False)
    date_post: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=func.now())
    user_id: Mapped[int] = mapped_column(ForeignKey("user.user_id"), nullable=False)

    advertisement = relationship(User, backref="user")

Base.metadata.create_all(bind=engine)
