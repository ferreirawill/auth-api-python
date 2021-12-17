from src.models.user_model import User,UserType,UserAndTypeAssociation
from src.services.database.connection import DeclarativeBase,DatabaseConnection

import unittest


class MyTestCase(unittest.TestCase):
    def testUserCreation(self):
        instance = DatabaseConnection.getInstance()
        DeclarativeBase.metadata.create_all(instance.engine)

        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
