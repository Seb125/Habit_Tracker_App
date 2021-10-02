''' In this module all classes of the habit tracker are defined.'''

from datetime import date, timedelta, datetime
from prettytable import PrettyTable

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
        try:
            if x[1] == "good":
                if x[2] == "daily":
                    new_habit = Daily_habit(x[0], x[1], x[2], [], [])
                    self.good_daily_habits.append(new_habit)
                elif x[2] == "weekly":
                    new_habit = Weekly_habit(x[0], x[1], x[2], [], [])
                    self.good_weekly_habits.append(new_habit)
                elif x[2] == "monthly":
                    new_habit = Monthly_habit(x[0], x[1], x[2], [], [])
                    self.good_monthly_habits.append(new_habit)
            elif x[1] == "bad":
                new_habit = Bad_habit(x[0], x[1], [], [])
                self.bad_habits.append(new_habit)
            self.all_habits.append(new_habit)
        except IndexError:
            print("Please check the instructions for creating a new habit!")

    def delete_habit(self):
        '''This mehtod deletes a habit from the habit profile.'''

        habit = input()
        for i, h in enumerate(self.all_habits):
            if h.name == habit:
                del self.all_habits[i]
        for i, h in enumerate(self.good_daily_habits):
            if h.name == habit:
                del self.good_daily_habits[i]
        for i, h in enumerate(self.good_weekly_habits):
            if h.name == habit:
                del self.good_weekly_habits[i]
        for i, h in enumerate(self.good_monthly_habits):
            if h.name == habit:
                del self.good_monthly_habits[i]
        for i, h in enumerate(self.bad_habits):
            if h.name == habit:
                del self.bad_habits[i]


    def summary(self):
        '''This method provides an overview over all habits in the habit profile.'''

        # Here the number of days of the previous month are calculated
        today = date.today()
        first = today.replace(day=1)
        lastMonth = first - timedelta(days=1)
        number_days_last_month = (date(first.year, first.month, 1) - date(lastMonth.year, lastMonth.month, 1)).days

        # For Bad habits the number of no breaks in the last month is equal to the number of days minus the number of dates in the list
        x = PrettyTable()
        x.add_column("Habit",[habit.name for habit in self.all_habits])
        x.add_column("Since",[habit.creation_date for habit in self.all_habits])
        x.add_column("Periodicity", [habit.period if habit.quality == "good" else "X" for habit in self.all_habits])
        x.add_column("Current_streak_length",[habit.streaks()[0] for habit in self.all_habits])
        x.add_column("Maximum_streak_length", [habit.streaks()[1] for habit in self.all_habits])
        x.add_column("Sucess_rate_last_month", [habit.number_no_breaks_last_month() if habit.quality == "good"
                                                         else (number_days_last_month - habit.number_no_breaks_last_month()) for habit in self.all_habits])

        # Here a list of the habits which have the longest streak length is created
        streak_lengths = [habit.streaks()[1] for habit in self.all_habits]
        max_streak_length = max(streak_lengths)
        max_list = []
        for i, h in enumerate(streak_lengths):
            if h == max_streak_length:
                max_list.append(self.all_habits[i].name)

        print(x)
        print("Your habit(s) with the longest streak: {habit}".format(habit = max_list))

class Habit:
    '''This class is the superclass of all good and bad habits.'''

    def __init__(self, name, quality, dates, time):
        self.name = name
        self.quality = quality
        self.dates = dates
        self.time = time
        self.creation_date = date.today()

    def generate_table(self):
        '''Here an overview of all the saved dates for a single habit is created'''

        y = PrettyTable()
        if self.quality == "good":
            print("Days, on which you finished your {period} routine for habit \'{habit}\' :".format(period = self.period, habit = self.name)+ "\n")
        else:
            print("Days, on which you could'nt avoid your habit \'{habit}\' :".format(habit=self.name) + "\n")
        y.add_column("Dates", self.dates)
        y.add_column("Time", self.time)
        print(y)
        print("\nYour current streak is {time} periods long!\n".format(time=self.streaks()[0]))
        print("Your maximum streak is {time} periods long!".format(time=self.streaks()[1]))

    def number_no_breaks_last_month(self):
        '''Here the number of days on which a habit was performed in the last month is calculated'''

        today = str(date.today())
        today_split = today.split("-")
        last_month = int(today_split[1]) - 1
        no_break = []
        for d in self.dates:
            date_split = str(d).split("-")
            if last_month == int(date_split[1]) and datetime.now().year == int(date_split[0]):
                no_break.append(d) # Every date in the list, which has the same year and month as the last month, is saved in the list "no_break"
        return len(no_break)

    def check_off_habit(self):
        '''This method checks of a habit'''

        today = date.today()
        if not self.dates:
            self.dates.append(today)
            self.time.append(datetime.now())
        elif self.quality == "good":
            if 1 > self.delta_periods(): # The current date is only saved in the profile, if the user is not in the current period
                print("You already finished this habit for the current period")
            else:
                self.dates.append(today)
                self.time.append(datetime.now())
        else:                            # The same procedure for bad habits
            if self.dates[-1] == today:
                print("You have already indicated that you have followed this habit today")
            else:
                self.dates.append(today)
                self.time.append(datetime.now())

class Good_habit(Habit):
    '''This class is the superclass of all good habits (daiy, weekly, monthly)'''

    def streaks(self):
        '''This method returns the latest and the maximum streak of a good habit'''

        counter = 0
        streaks = [0]
        if not self.dates:
            return counter, max(streaks)

        elif self.period == "daily":
            counter = 1
            for i in range(len(self.dates)-1):
                if (self.dates[i+1] - self.dates[i]).days == 1:
                    counter += 1  # The counter is increased as long as the difference between two consecutive dates is not greater than one day
                else:
                    streaks.append(counter)
                    counter = 1
            streaks.append(counter)
            if abs((self.dates[-1] - date.today()).days) < 2: # For a diffeerence of mor than one day the user breaks the habit
                return counter, max(streaks) # Returns current streak, maximum streak
            else:
                return 0, max(streaks) # If there is a gap of more than one day between the last date and the current date the current streak is set to 0
        elif self.period == "weekly":
            counter = 1
            for i in range(len(self.dates)-1):
                monday1 = (self.dates[i] - timedelta(days=self.dates[i].weekday())) # This is the Monday in the same week as self.dates[i]
                monday2 = (self.dates[i+1] - timedelta(days=self.dates[i+1].weekday())) # This is the Monday in the same week as self.dates[i+1]
                if (monday2 - monday1).days / 7 < 2: # For a difference of more than 1 calendar week between two Mondays the user breaks the habit
                    counter += 1
                else:
                    streaks.append(counter)
                    counter = 1
            streaks.append(counter)
            last_monday = (date.today() - timedelta(days=date.today().weekday()))
            last_monday_in_dates = (self.dates[-1] - timedelta(days=self.dates[-1].weekday()))
            if (last_monday - last_monday_in_dates).days / 7 < 2:
                return counter, max(streaks)
            else:
                return 0, max(streaks)
        elif self.period == "monthly":
            counter = 1
            for i in range(len(self.dates) - 1):
                if self.diff_month(self.dates[i + 1], self.dates[i]) == 1: # diff_month is a method of class Monthly_habit
                    counter += 1
                else:
                    streaks.append(counter)
                    counter = 1
            if self.diff_month(self.dates[-1], date.today()) < 2:
                return counter, max(streaks)
            else:
                return 0, max(streaks)

class Bad_habit(Habit):

    def streaks(self):
        '''This method returns the latest and the maximum streak of a bad habit'''

        streaks = [0]
        if not self.dates:  # If the list is empty the user did not break the habit yet
            return (self.creation_date - date.today()).days, (self.creation_date - date.today()).days
        else:
            for i in range(len(self.dates) - 1):
                if (self.dates[i + 1] - self.dates[i]).days != 1: # For two dates on consecutive days there is no streak
                    streaks.append((self.dates[i + 1] - self.dates[i]).days)
            max_streak = max(streaks)
            current_streak = (date.today() - self.dates[-1]).days
            if current_streak > max_streak:
                max_streak = current_streak
            return current_streak, max_streak

class Daily_habit(Good_habit, Habit):

    def __init__(self, name, quality, period, dates, time):
        self.period = period
        super().__init__(name, quality, dates, time)

    def delta_periods(self):
        '''This method returns the number of periods between the last entry in the dates-list and the current date'''

        today = date.today()
        last_entry = self.dates[-1]
        time_diff = (today - last_entry).days
        return time_diff

class Weekly_habit(Good_habit, Habit):

    def __init__(self, name, quality, period, dates, time):
        self.period = period
        super().__init__(name, quality, dates, time)

    def delta_periods(self):
        '''This method returns the number of periods between the last entry in the dates-list and the current date'''

        time_diff = ((date.today() - timedelta(days=date.today().weekday())) - (self.dates[-1] - timedelta(days=self.dates[-1].weekday()))).days / 7
        return time_diff

class Monthly_habit(Good_habit, Habit):

    def __init__(self, name, quality, period, dates, time):
        self.period = period
        super().__init__(name, quality, dates, time)

    def diff_month(self, d1, d2):
        '''This method returns the number of months bewteen two dates d1 and d2'''

        return abs((d1.year - d2.year) * 12 + d1.month - d2.month)

    def delta_periods(self):
        '''This method returns the number of periods between the last entry in the dates-list and the current date'''

        today = date.today()
        last_entry = self.dates[-1]
        return self.diff_month(today, last_entry)