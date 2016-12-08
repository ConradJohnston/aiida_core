from aiida.backends.sqlalchemy.tests.testbase import SqlAlchemyTests
from aiida.backends.tests.restapi import ImportDataSetUp, RESTApiTestSuit

class LocalSetup(SqlAlchemyTests, ImportDataSetUp):
    """

    """
    @classmethod
    def setUpClass(cls):
        for base in LocalSetup.__bases__:
            base.setUpClass()

        from aiida.orm.computer import Computer
        info = {
            "name": "test1",
            "hostname": "test1.epfl.ch",
            "transport_type":'ssh',
            "scheduler_type":'torque',
            "workdir": '/tmp/aiida'
        }
        cls.computer = Computer(**info)
        cls.computer.store()


class SqlaRESTApiTestSuit(LocalSetup, RESTApiTestSuit):
    """

    """
    pass
