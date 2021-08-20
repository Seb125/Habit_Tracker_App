''' In this module all classes of the habit tracker are defined.'''

from datetime import date, timedelta
from pandas import DataFrame

class Habit_profile:
    '''This class contains all instances of the habit profile.'''

    def __init__(self, name):
        self.name = name
        self.good_daily_habits = []
        self.good_weekly_habits = []
        self.good_monthly_habits = []
        self.bad_habits = []
        self.all_habits = []

    def create_habit(self):
        '''This method creates a new habit and saves it in the habit profile.'''

        habit_name = input()
        x = habit_name.split()
        if x[1] == "good":
            if x[2] == "daily":
                new_habit = Daily_habit(x[0], x[1], x[2], [])
                self.good_daily_habits.append(new_habit)
            elif x[2] == "weekly":
                new_habit = Weekly_habit(x[0], x[1], x[2], [])
                self.good_weekly_habits.append(new_habit)
            elif x[2] == "monthly":
                new_habit = Monthly_habit(x[0], x[1], x[2], [])
                self.good_monthly_habits.append(new_habit)
        elif x[1] == "bad":
            new_habit = Bad_habit(x[0], x[1], [])
            self.bad_habits.append(new_habit)
        self.all_habits.append(new_habit)

    def delete_habit(self):
        '''This mehtod deletes a habit form the habit profile.'''

        nhabit = input()
        x = nhabit.split()
        for i, h in enumerate(self.all_habits):
            if h.name == x[0]:
                del self.all_habits[i]

    def summary(self):
        '''This method provides an overview over all habits in the habit profile.'''

        # Here the number of days of the previous month are calculated
        today = date.today()
        first = today.replace(day=1)
        lastMonth = first - timedelta(days=1)
        number_days_last_month = (date(first.year, first.month, 1) - date(lastMonth.year, lastMonth.month, 1)).days

        # For Bad habits the number of successes is equal to the number days minus the number of dates in the list
        data = {"Habit": [habit.name for habit in
         self.all_habits], "Since": [habit.creation_date for habit in
         self.all_habits], "Current_streak_length": [habit.streaks()[0] for habit in
         self.all_habits], "Maximum_streak_length": [habit.streaks()[1] for habit in
         self.all_habits], "Relative_sucess_rate_last_month": [str(habit.number_no_breaks_last_month()) + "/" + str(number_days_last_month) for habit in
         self.good_daily_habits] + [str(habit.number_no_breaks_last_month()) + "/" + str(int(number_days_last_month/7)) for habit in
         self.good_weekly_habits] + [str(number_days_last_month - habit.number_no_breaks_last_month()) + "/" + str(number_days_last_month) for habit in
         self.bad_habits] + [str(habit.number_no_breaks_last_month()) + "/" + str(1) for habit in
         self.good_monthly_habits]}
        data_frame = DataFrame(data)

        # Here a list of the habits which have the longest streak length is created
        max_streak_length = max(data_frame["Maximum_streak_length"])
        max_list = []
        for i, h in enumerate(data_frame["Maximum_streak_length"]):
            if h == max_streak_length:
                max_list.append(data_frame["Habit"][i])

        print("")
        print("--------------------------------------------------------------------------------")
        print(data_frame)
        print("")
        print("--------------------------------------------------------------------------------")
        print("Your habit(s) with the longest streak: {habit}".format(habit = max_list))
        print("")

class Habit:
'''This class is the superclass of all good and bad habits.'''

    def __init__(self, name, quality, dates):
        self.name = name
        self.quality = quality
        self.dates = dates
        self.creation_date = date.today()

    # Here an overview of all the saved dates for a single habit is created
    def generate_table(self):
        print("--------------------------------------------------------------------------------")
        dates = {"Dates": self.dates}
        df = DataFrame(dates, columns = ["Dates"])
        if self.quality == "good":
            print("Days, on which you finished your {period} routine for habit \'{habit}\' :".format(period = self.period, habit = self.name)+ "\n")
        else:
            print("Days, on which you could'nt avoid your habit \'{habit}\' :".format(habit=self.name) + "\n")
        print(df)
        print("\nYour current streak is {time} periods long!\n".format(time=self.streaks()[0]))
        print("Your maximum streak is {time} periods long!".format(time=self.streaks()[1]))

    # Here the number of days on which a habit was performed in the last month is calculated
    def number_no_breaks_last_month(self):
        today = str(date.today())
        today_split = today.split("-")
        last_month = int(today_split[1]) - 1
        no_break = []
        for d in self.dates:
            date_split = str(d).split("-")
            if last_month == int(date_split[1]):
                no_break.append(d)
        return len(no_break)

    # This method checks of a habit
    def check_off_habit(self):
        today = date.today()
        if not self.dates:
            self.dates.append(today)
        elif self.quality == "good":
            if 1 > self.delta_periods():
                print("You already finished this habit for the current period")
            else:
                self.dates.append(today)
        else:
            if self.dates[-1] == today:
                print("You have already indicated that you have followed this habit today")
            else:
                self.dates.append(today)

class Good_habit(Habit):

    # This method returns the latest and the maximum streak of a good habit
    def streaks(self):
        counter = 0
        streaks = [0]
        if not self.dates:
            return counter, max(streaks)

        elif self.period == "daily":
            counter = 1
            for i in range(len(self.dates)-1):
                if (self.dates[i+1] - self.dates[i]).days == 1:
                    counter += 1
                else:
                    streaks.append(counter)
                    counter = 1
            streaks.append(counter)

        elif self.period == "weekly":
            counter = 1
            for i in range(len(self.dates)-1):
                if (self.dates[i+1] - self.dates[i]).days < 8:     # for a difference of more than 7 days, the user breaks the habit
                    counter += 1
                else:
                    counter = 1
                    streaks.append(counter)
            streaks.append(counter)

        elif self.period == "monthly":
            counter = 1
            for i in range(len(self.dates) - 1):
                if self.diff_month(self.dates[i + 1], self.dates[i]) == 1:
                    counter += 1
                else:
                    counter = 1
                    streaks.append(counter)
            streaks.append(counter)

        return counter, max(streaks)

class Bad_habit(Habit):

    # This method returns the latest and the maximum streak of a bad habit
    def streaks(self):
        streaks = [0]
        # If the list is empty the user did not break is habit yet
        if not self.dates:
            return (self.creation_date - date.today()).days, (self.creation_date - date.today()).days
        else:
            for i in range(len(self.dates) - 1):
                if (self.dates[i + 1] - self.dates[i]).days != 1:
                    streaks.append((self.dates[i + 1] - self.dates[i]).days)
            max_streak = max(streaks)
            current_streak = (date.today() - self.dates[-1]).days
            if current_streak > max_streak:
                max_streak = current_streak
            return current_streak, max_streak

class Daily_habit(Good_habit, Habit):

    def __init__(self, name, quality, period, dates):
        self.period = period
        super().__init__(name, quality, dates)

    # This method returns the number of periods between the last entry in the dates-list and the current date
    def delta_periods(self):
        today = date.today()
        last_entry = self.dates[-1]
        time_diff = (today - last_entry).days
        return time_diff

class Weekly_habit(Good_habit, Habit):

    def __init__(self, name, quality, period, dates):
        self.period = period
        super().__init__(name, quality, dates)

    # This method returns the number of periods between the last entry in the dates-list and the current date
    def delta_periods(self):
        today = date.today()
        last_entry = self.dates[-1]
        time_diff = (today - last_entry).days
        return time_diff/7

class Monthly_habit(Good_habit, Habit):

    def __init__(self, name, quality, period, dates):
        self.period = period
        super().__init__(name, quality, dates)

    # This method returns the number of months bewteen two dates d1 and d2
    def diff_month(self, d1, d2):
        return abs((d1.year - d2.year) * 12 + d1.month - d2.month)

    # This method returns the number of periods between the last entry in the dates-list and the current date
    def delta_periods(self):
        today = date.today()
        last_entry = self.dates[-1]
        return self.diff_month(today, last_entry)