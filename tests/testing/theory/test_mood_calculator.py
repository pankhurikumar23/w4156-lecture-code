import unittest
from lectures.testing.theory.mood_calculator import MoodCalculator


class MyTestCase(unittest.TestCase):
    """
    Note - we have two methods beginning 'test'. Both these methods will be run
    """

    def setUp(self):
        self.mood_calculator = MoodCalculator()

    def test_out_of_range(self):
        with self.assertRaises(ValueError):
            # print("Inside")
            self.mood_calculator.calculate_mood(-1, 70)
            self.mood_calculator.calculate_mood(0, 91)

    def test_mood_calculator(self):
        """
        TODO - Exercise for the student to write and test the mood calculator
        :return:
        """
        cases = [(0, 70, "Irritated"),
                 (0, 75, "Irritated"),
                 (0, 76, "Joyful"),
                 (0, 90, "Joyful"),
                 (26, 70, "Irritated"),
                 (26, 75, "Irritated"),
                 (26, 76, "Joyful"),
                 (26, 90, "Joyful"),
                 (27, 70, "Grumpy"),
                 (27, 75, "Grumpy"),
                 (27, 76, "Hulk"),
                 (27, 90, "Hulk"),
                 (36, 70, "Grumpy"),
                 (36, 75, "Grumpy"),
                 (36, 76, "Hulk"),
                 (36, 90, "Hulk")
                 # Following values give valueError:
                 # , (-1, 70, "Error"),
                 # (37, 70, "Error"),
                 # (0, 69, "Error"),
                 # (0, 91, "Error"),
                 ]

        list(map(lambda x: self.push_assert(x[0], x[1], x[2]), cases))

    def push_assert(self, sleepDeprivation, bloodSugar, expected):
        self.assertEqual(self.mood_calculator.calculate_mood(sleepDeprivation,  bloodSugar), expected)


if __name__ == '__main__':
    unittest.main()
