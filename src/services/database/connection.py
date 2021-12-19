from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os



class DatabaseConnection:
    __instance = None
    engine = None  # Recebe a conexão
    session = None  # Recebe a sessão da conexão
    Base = declarative_base()  # Recebe uma clase de para criar os models

    def __init__(self):
        if DatabaseConnection.__instance is not None:
            raise Exception("This class is a singleton")
        else:
            DatabaseConnection.__instance = self

    @staticmethod
    def getInstance():
        if DatabaseConnection.__instance is None:
            __instance = DatabaseConnection()
            __instance.__initDatabase()
        return DatabaseConnection.__instance

    def __initDatabase(self):
        connectionString = os.environ.get("DB_CONNECTION_STRING")
        if connectionString is None:
            connectionString = "postgresql+psycopg2://postgres:54321@localhost:5432/sqlalchemy_Tests"

        if not database_exists(connectionString):
            create_database(connectionString)
        else:
            self.engine = create_engine(connectionString)

        self.engine = create_engine(connectionString)
        Session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.session: Session = Session()

        self.Base.metadata.create_all(self.engine)

