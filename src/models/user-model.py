from sqlalchemy import Column, Integer,String,Boolean
from ..services.database.connection import DatabaseConnection


class User(DatabaseConnection.Base):
    __tablename__ = "Users"

    id = Column(Integer,primary_key=True,index=True)
    email = Column(String,unique=True,index=True)
    hashedPasswod = Column(String)
    isActive = Column(Boolean,default=True)
