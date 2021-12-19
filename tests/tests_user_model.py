from src.models.user_model import User, UserType, UserAndTypeAssociation
from src.services.database.connection import DatabaseConnection
from sqlalchemy import  select
import unittest


class UserTestAcse(unittest.TestCase):
    def testUserTypeCreation(self):
        instance: DatabaseConnection = DatabaseConnection.getInstance()
        instance.session.add(UserType(name="Diretor"))
        instance.session.add(UserType(name="Comercial"))
        instance.session.add(UserType(name="Suporte"))
        instance.session.add(UserType(name="Gerente"))
        instance.session.add(UserType(name="CEO"))
        instance.session.commit()
        instance.engine.dispose()

    def testUserCreation(self):
        instance: DatabaseConnection = DatabaseConnection.getInstance()

        instance.session.add(
            User(name="lhais", email="lhaizam@gmail.com", hashedPassword="lldghjlweialjk",
                 isActive=True))
        instance.session.commit()

    def testReadUserType(self):
        instance: DatabaseConnection = DatabaseConnection.getInstance()
        query = instance.session.query(UserType).all()
        print(UserType.listToJson(query))

    def testReadUser(self):
        instance: DatabaseConnection = DatabaseConnection.getInstance()
        query = instance.session.query(User).all()
        print(User.listToJson(query))

    def testCreateUserAndTypRelation(self):
        instance: DatabaseConnection = DatabaseConnection.getInstance()
        instance.session.add(UserAndTypeAssociation(userId= 2,userTypeId=5))
        instance.session.commit()

    def testReadUserWithJoin(self):
        instance: DatabaseConnection = DatabaseConnection.getInstance()
        #query = select(User.name,User.email,UserType.name).join(User.types)

        query = 'select "Users".name,"Users".email, "UserType".name from "Users" join "UserTypeAssociation" on "Users".id = ' \
                '"UserTypeAssociation"."userId" join "UserType" on "UserType".id = "UserTypeAssociation"."userTypeId"; '

        print(query)
        queryResult = instance.session.execute(query)

        for rowTuple in queryResult:
            print(rowTuple)


if __name__ == '__main__':
    unittest.main()
