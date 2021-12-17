from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ..services.database.connection import DeclarativeBase


class User(DeclarativeBase):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    hashedPasswod = Column(String)
    types = relationship("UserAndTypeAssociation")
    isActive = Column(Boolean, default=True)


class UserType(DeclarativeBase):
    __tablename__ = "UserType"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)


class UserAndTypeAssociation(DeclarativeBase):
    __tablename__ = "UserTypeAssociation"

    userId = Column(ForeignKey("Users.id"), primary_key=True)
    userTypeId = Column(ForeignKey("UserType.id"), primary_key=True)
    userType = relationship("UserType")
