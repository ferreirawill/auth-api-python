from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from ..services.database.connection import DatabaseConnection
from sqlalchemy.orm import relationship


class User(DatabaseConnection.Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    hashedPassword = Column(String)
    types = relationship("UserAndTypeAssociation",backref="usertype")
    isActive = Column(Boolean, default=True)
    @staticmethod
    def listToJson(userList):
        jsonList = []
        for user in userList:
            jsonList.append({
                "id": user.id,
                "name":user.name,
                "email":user.email,
                "types":UserAndTypeAssociation.listToJson(user.types),
                "isActive":user.isActive
            })
        return jsonList

    @staticmethod
    def toJson(user):
        return {
                "id": user.id,
                "name":user.name,
                "email":user.email,
                "types":UserAndTypeAssociation.listToJson(user.types),
                "isActive":user.isActive
            }


class UserType(DatabaseConnection.Base):
    __tablename__ = "UserType"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)

    @staticmethod
    def listToJson(typeList):
        jsonList = []
        for userType in typeList:
            jsonList.append({
                "userType":userType.name,
                "id":userType.id
            })
        return jsonList

    @staticmethod
    def toJson(typeModel):
        return {
            "userType": typeModel.name,
            "id": typeModel.id
        }


class UserAndTypeAssociation(DatabaseConnection.Base):
    __tablename__ = "UserTypeAssociation"

    userId = Column(ForeignKey("Users.id"), primary_key=True)
    userTypeId = Column(ForeignKey("UserType.id"), primary_key=True)
    userType = relationship("UserType")

    @staticmethod
    def listToJson(associationList):
        jsonList = []
        for associationType in associationList:
            jsonList.append({
                "typeId":associationType.userTypeId
            })
        return jsonList
