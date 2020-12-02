import unittest
from unittest.mock import *
from src.checker import Checker


class TestChecker(unittest.TestCase):

    def test_played_before_17(self):
        # prepare mock
        self.checker.environment.getTime = Mock(name='getTime')
        self.checker.environment.getTime.return_value = 16
        self.checker.environment.resetWav = Mock(name='resetWav')
        self.checker.environment.resetWav.return_value = False

        # testing
        self.assertEqual(self.checker.remainder("dog_snoring_into_echo_microphone.wav"), False)

    def test_played_after_17(self):
        # prepare mock
        self.checker.environment.getTime = Mock(name='getTime')
        self.checker.environment.getTime.return_value = 18
        self.checker.environment.wavWasPlayed = Mock(name='wavWasPlayed')
        self.checker.environment.wavWasPlayed.return_value = True

        # testing
        self.assertEqual(self.checker.remainder("dog_snoring_into_echo_microphone.wav"), True)

    def setUp(self):
        self.checker = Checker()

    def tearDown(self):
        self.checker = None


if __name__ == '__main__':
    unittest.main()
