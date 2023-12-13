# from app.models import Base
# from app.config import POSTGRES_DB, POSTGRES_HOST, POSTGRES_PASSWORD, POSTGRES_PORT, POSTGRES_USER
#
# class Database:
#     def __init__(self):
#         self.bd = postgresql
#         self.bd_host = POSTGRES_HOST
#         self.bd_port = POSTGRES_PORT
#         self.bd_name = POSTGRES_DB
#         self.bd_username = POSTGRES_USER
#         self.bd_pass = POSTGRES_PASSWORD
#
#     def create_conect(self):
#         dsn = "{}://{}:{}@{}:{}/{}".format(self.bd, self.bd_username, self.bd_pass, self.bd_host, self.bd_port, self.bd_name)
#         return dsn
#
#     def create_tables(self, engine):
#         Base.metadata.drop_all(engine)
#         Base.metadata.create_all(engine)
