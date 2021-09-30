import unittest
from classes_Kopie import *
from main import load_data

test_profile = input()

class TestCalc(unittest.TestCase):

    def setUp(self):
       self.profile = load_data("sample_data.pkl")

    def test_number_no_breaks_last_month(self):
        self.assertEqual(self.profile.good_daily_habits[0].number_no_breaks_last_month(), 4)
        self.assertEqual(self.profile.good_weekly_habits[0].number_no_breaks_last_month(), 1)
        self.assertEqual(self.profile.good_monthly_habits[0].number_no_breaks_last_month(), 1)
        self.assertEqual(self.profile.bad_habits[0].number_no_breaks_last_month(), 0)
        self.assertEqual(self.profile.good_daily_habits[1].number_no_breaks_last_month(), 3)

    def test_streaks(self):
        self.assertEqual(self.profile.good_daily_habits[0].streaks()[0], 0)
        self.assertEqual(self.profile.good_daily_habits[0].streaks()[1], 4)
        self.assertEqual(self.profile.good_weekly_habits[0].streaks()[0], 0)
        self.assertEqual(self.profile.good_weekly_habits[0].streaks()[1], 3)
        self.assertEqual(self.profile.good_monthly_habits[0].streaks()[0], 2)
        self.assertEqual(self.profile.good_monthly_habits[0].streaks()[1], 4)
        self.assertEqual(self.profile.bad_habits[0].streaks()[0], 1)
        self.assertEqual(self.profile.bad_habits[0].streaks()[1], 366)
        self.assertEqual(self.profile.good_daily_habits[1].streaks()[0], 1)
        self.assertEqual(self.profile.good_daily_habits[1].streaks()[1], 5)

    def test_core_functions(self):
        '''To test the core functions of the habit tracker, input as specified below is required when running the programm.'''

        self.profile.create_habit()  # Create any new habit you like
        self.assertIsInstance(self.profile.all_habits[-1], Habit)
        new_habit = self.profile.all_habits[-1]
        self.profile.delete_habit()  # Here you need to provide the name of the recently created habit
        self.assertNotIn(new_habit, self.profile.all_habits)
        self.profile.good_daily_habits[0].check_off_habit()
        self.assertEqual(self.profile.good_daily_habits[0].dates[-1], date.today())


if __name__ == '__main__':
    unittest.main()
