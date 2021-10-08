import unittest
from classes_Kopie import *
from datetime import date


class TestCalc(unittest.TestCase):

    def setUp(self):

        self.workout_data = [date(2021, 1, 1), date(2021, 1, 2), date(2021, 1, 3), date(2021, 1, 4), date(2021, 2, 1),
                        date(2021, 2, 3), date(2021, 2, 5), date(2021, 7, 1), date(2021, 8, 25), date(2021, 8, 26),
                        date(2021, 8, 27), date(2021, 8, 28)]
        self.gaming_data = [date(2021, 1, 1), date(2021, 1, 8), date(2021, 1, 16), date(2021, 2, 4), date(2021, 2, 9),
                       date(2021, 2, 23), date(2021, 8, 29)]
        self.hiking_data = [date(2020, 12, 1), date(2021, 1, 8), date(2021, 2, 16), date(2021, 3, 4), date(2021, 5, 9),
                       date(2021, 7, 23), date(2021, 8, 31)]
        self.smoking_data = [date(2020, 8, 1), date(2020, 9, 3), date(2020, 9, 4), date(2020, 9, 5), date(2020, 9, 6),
                        date(2021, 9, 7), date(2021, 9, 8), date(2021, 9, 9), date(2021, 9, 10), date(2021, 9, 28)]
        self.homework_data = [date(2021, 8, 25), date(2021, 8, 26), date(2021, 8, 27), date(2021, 8, 28), date(2021, 9, 3),
                         date(2021, 9, 4), date(2021, 9, 5), date(2021, 9, 6), date(2021, 9, 7), date(2021, 9, 8),
                         date(2021, 9, 9), date(2021, 9, 10), date(2021, 9, 11), date(2021, 9, 28)]

        self.workout = Daily_habit("workout", "good", "daily", self.workout_data, [])
        self.gaming = Weekly_habit("gaming", "good", "weekly", self.gaming_data, [])
        self.hiking = Monthly_habit("hiking", "good", "monthly", self.hiking_data, [])
        self.smoking = Bad_habit("smoking", "bad", self.smoking_data, [])
        self.homework = Daily_habit("homework", "good", "daily", self.homework_data, [])

    def test_number_no_breaks_last_month(self):
        '''Here the analytic method to calculate the number of successes in the last month is tested'''

        self.assertEqual(self.workout.number_no_breaks_last_month(), 0)
        self.assertEqual(self.gaming.number_no_breaks_last_month(), 0)
        self.assertEqual(self.hiking.number_no_breaks_last_month(), 0)
        self.assertEqual(self.smoking.number_no_breaks_last_month(), 5) # For a bad habit these are actually the number of breaks
        self.assertEqual(self.homework.number_no_breaks_last_month(), 10)

    def test_streaks(self):
        '''Here the analytic methods to calculate the current and the maximum streak are tested'''

        self.assertEqual(self.workout.streaks()[0], 0) # streaks[0] returns the current streak
        self.assertEqual(self.workout.streaks()[1], 4) # streaks[1] returns the maximum streak
        self.assertEqual(self.gaming.streaks()[0], 0)
        self.assertEqual(self.gaming.streaks()[1], 3)
        self.assertEqual(self.hiking.streaks()[0], 0)
        self.assertEqual(self.hiking.streaks()[1], 4)
        self.assertEqual(self.smoking.streaks()[0], 3)
        self.assertEqual(self.smoking.streaks()[1], 366)
        self.assertEqual(self.homework.streaks()[0], 0)
        self.assertEqual(self.homework.streaks()[1], 9)

    def test_core_functions(self):
        '''Here the core functions of the habit tracker are tested'''

        self.assertIsInstance(self.workout, Habit) # Check if an object of class Habit was created
        self.assertIsInstance(self.workout, Daily_habit) # Check if an object of class Daily_habit(Habit) was created
        self.assertIsInstance(self.gaming, Habit)
        self.assertIsInstance(self.gaming, Weekly_habit)
        self.assertIsInstance(self.hiking, Habit)
        self.assertIsInstance(self.hiking, Monthly_habit)
        self.assertIsInstance(self.smoking, Habit)
        self.assertIsInstance(self.smoking, Bad_habit)
        self.assertIsInstance(self.homework, Habit)
        self.assertIsInstance(self.homework, Daily_habit)

        self.workout.check_off_habit()
        self.smoking.check_off_habit()
        self.assertEqual(self.workout.dates[-1], date.today())  # Check if the last date in the list is equal to todays date
        self.assertEqual(self.smoking.dates[-1], date.today())

if __name__ == '__main__':
    unittest.main()
