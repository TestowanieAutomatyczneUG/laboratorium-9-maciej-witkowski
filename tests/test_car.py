import unittest
from unittest.mock import *
from car import *


class TestCar(unittest.TestCase):

    def test_needsFuel_true(self):
        # prepare mock
        self.car.needsFuel = Mock(name='needsFuel')
        self.car.needsFuel.return_value = True

        # testing
        self.assertEqual(self.car.needsFuel(), True)

    def test_needsFuel_false(self):
        # prepare mock
        self.car.needsFuel = Mock(name='needsFuel')
        self.car.needsFuel.return_value = False

        # testing
        self.assertEqual(self.car.needsFuel(), False)

    @patch.object(Car, 'getEngineTemperature')
    def test_getEngineTemperature(self, mock):
        mock.return_value = 85
        result = self.car.getEngineTemperature()
        self.assertEqual(result, 85)

    def setUp(self):
        self.car = Car()

    def tearDown(self):
        self.car = None


if __name__ == '__main__':
    unittest.main()
