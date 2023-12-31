import unittest
import TestingExercise

class TestTestingExercise(unittest.TestCase):
    def setUp(self):
        print('starting testing')

    def test_guessing_function_correct_guess(self):
        random_number = 5
        guessed_number = 5
        result = TestingExercise.guessing_function(random_number, guessed_number)
        self.assertTrue(result)

    def test_guessing_function_wrong_guess(self):
        random_number = 5
        guessed_number = 1
        result = TestingExercise.guessing_function(random_number, guessed_number)
        self.assertFalse(result)

    def test_guessing_function_wrong_number(self):
        random_number = 5
        guessed_number = 11
        result = TestingExercise.guessing_function(random_number, guessed_number)
        self.assertFalse(result)

    def test_guessing_function_wrong_input_type(self):
        random_number = 5
        guessed_number = '11'
        result = TestingExercise.guessing_function(random_number, guessed_number)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()



