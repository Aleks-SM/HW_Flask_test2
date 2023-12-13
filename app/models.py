import datetime
from sqlalchemy import String, DateTime, func, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from config import POSTGRES_PASSWORD, POSTGRES_USER, POSTGRES_DB, POSTGRES_PORT, POSTGRES_HOST


PG_DSN = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
engine = create_engine(PG_DSN)
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    registration_time: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=func.now())

    def is_authenticated():
        return True

    def is_active():
        return True

    def is_anonymous():
        return False

    def get_id(self):
        return str(self.id)
        
    @property
    def dict(self):
        return {
            'user_id': self.id,
            'name': self.name,
            'email': self.email,
            'registration_time': self.registration_time.isoformat()
        }

class Advertisement(Base):
    __tablename__ = "advertisement"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(20), nullable=False)
    description: Mapped[str] = mapped_column(String(120), nullable=False)
    date_post: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=func.now())
    owner_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete='CASCADE'), nullable=False)

    user = relationship("User", backref="user")

Base.metadata.create_all(bind=engine)
