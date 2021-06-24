from datetime import date, timedelta
import datetime
from pandas import DataFrame


class Habit_profile:
    "This class creates instances of habit_profiles"
    def __init__(self, name):
        self.name = name
        self.good_daily_habits = []
        self.good_weekly_habits = []
        self.bad_habits = []
        self.all_habits = []

    def create_delete_habit(self):
        nhabit = input()
        x = nhabit.split()
        new = True
        for i, h in enumerate(self.all_habits):
            if h.name == x[0]:
                del self.all_habits[i]
                new = False
        if new:
            if x[1] == "good":
                if x[2] == "daily":
                    new_habit = Daily_habit(x[0], x[1], x[2], [])
                    self.good_daily_habits.append(new_habit)
                elif x[2] == "weekly":
                    new_habit = Weekly_habit(x[0], x[1], x[2], [])
                    self.good_weekly_habits.append(new_habit)
            elif x[1] == "bad":
                new_habit = Bad_habit(x[0], x[1], [])
                self.bad_habits.append(new_habit)
            print(new_habit)
            self.all_habits.append(new_habit)


    def summary(self):

        # Show current streak lengths of all habits

        for h in self.all_habits:
            h.current_streak_length= h.show_me_streak()

        # Show relative # of days, on which a habit was checked off
        # Get # of days of last month

        today = date.today()
        first = today.replace(day=1)
        datee = datetime.datetime.strptime(str(first), "%Y-%m-%d")
        lastMonth = first - datetime.timedelta(days=1)
        datee2 = datetime.datetime.strptime(str(lastMonth), "%Y-%m-%d")
        number_days_last_month = (date(datee.year, datee.month, 1) - date(datee2.year, datee2.month, 1)).days

        for h in self.all_habits:
            if h.quality == "good":
                h.no_breaks_last_month = str(h.rel_number_no_breaks_last_month()) + "/" + str(number_days_last_month)
            elif h.quality == "bad":
                h.no_breaks_last_month = str(number_days_last_month - h.rel_number_no_breaks_last_month()) + "/" + str(number_days_last_month)


        data = {"Habit": [habit.name for habit in
         self.good_daily_habits] + [habit.name for habit in self.good_weekly_habits] + [habit.name for habit in
         self.bad_habits], "Since": [habit.creation_date for habit in
         self.good_daily_habits] + [habit.creation_date for habit in self.good_weekly_habits] + [habit.creation_date for habit in
         self.bad_habits],
                "Current_streak_length": [habit.current_streak_length for habit in
         self.good_daily_habits] + [habit.current_streak_length for habit in self.good_weekly_habits] + [habit.current_streak_length for habit in
         self.bad_habits],
                "Relative_sucess_rate_last_month": [habit.no_breaks_last_month for habit in
         self.good_daily_habits] + [habit.no_breaks_last_month for habit in
         self.good_weekly_habits] + [habit.no_breaks_last_month for habit in
         self.bad_habits]}

        data_frame = DataFrame(data)
        print("")
        print("--------------------------------------------------------------------------------")
        print(data_frame)
        print("")
        print("--------------------------------------------------------------------------------")


class Habit:

    def __init__(self, name, quality, dates):

        self.name = name
        self.quality = quality
        self.dates = dates
        self.current_streak_length = 0
        self.no_breaks_last_month = 0
        self.creation_date = datetime.date.today()

    def generate_table(self):
        dataframe = {"Dates": self.dates}
        df = DataFrame(dataframe, columns = ["Dates"])

        print("Days, on which you finished your {period} routine for habit \'{habit}\' ".format(period = self.period, habit = self.name)+ "\n")
        print(df)

    def get_time_difference(self):

        today = datetime.date.today()
        last_entry = self.dates[-1]
        time_diff = (today - last_entry).days

        return time_diff

    def check_off_habit(self):
        today = date.today()

        if not self.dates:
            self.dates.append(today)

        else:

            diff = self.get_time_difference()

            print(diff)
            if 1 >= diff:
                print("You already finished this habit for the current period")
            else:
                for i in range(int(diff-1)):
                    self.dates.append("X")
                self.dates.append(today)

    def rel_number_no_breaks_last_month(self):
        today = str(date.today())
        today_split = today.split("-")
        last_month = int(today_split[1]) - 1
        no_break = []
        for d in self.dates:
            if d != "X":
                date_split = str(d).split("-")
                if last_month == int(date_split[1]):
                    no_break.append(d)

        return len(no_break)


class Good_habit(Habit):

    def show_me_streak(self):
        counter = 0
        for i in self.dates:
            if i == "X":
                counter = 0
            else:
                counter += 1
        return counter

class Bad_habit(Habit):

    def show_me_streak(self):
        counter = 0
        for i in self.dates:
            if i != "X":
                counter = 0
            else:
                counter += 1
        return counter


    def generate_table(self):
        dataframe = {"Dates": self.dates}
        df = DataFrame(dataframe, columns = ["Dates"])

        print("Days, on which you could'nt avoid your habit \'{habit}\' ".format(habit = self.name)+ "\n")
        print(df)

class Daily_habit(Good_habit, Habit):

    def __init__(self, name, quality, period, dates):
        self.period = period
        super().__init__(name, quality, dates)


class Weekly_habit(Good_habit, Habit):

    def __init__(self, name, quality, period, dates):
        self.period = period
        super().__init__(name, quality, dates)

    def check_off_habit(self):
        today = date.today()

        if not self.dates:
            self.dates.append(today)

        else:
            print(self.dates[0] )
            time_delta = (self.dates[-1] - self.dates[0]).days
            print(time_delta)
            remaining_weekdays = (7-(time_delta % 7))-1
            print(remaining_weekdays)
            time_delta2 = ((today - self.dates[-1]).days)-1 - remaining_weekdays
            print(time_delta2)

            if 1 >= time_delta2/7:
                print("You already finished this habit for the current period")
            else:
                for i in range(int(time_delta2/7)):
                    self.dates.append("X")
                self.dates.append(today)



