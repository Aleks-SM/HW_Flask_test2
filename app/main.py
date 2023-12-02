import sqlAlchemy as sq
from flask import flask
from database import Database


if __name__ == "__main__":
    bd_test = Database()
    engine = sq.create_engine(bd_test.create_conect())
    bd_test.create_tables(engine)
