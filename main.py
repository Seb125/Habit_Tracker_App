import argparse
import classes_Kopie as cl
import pickle
from datetime import date, timedelta



def load_data(name):
    "This function loads a saved habit_profile from a shelve"
    obj = pickle.load(open(name, 'rb'))
    return obj

def save_data(profile,name):
    "This function saves a habit_profile in a shelve"
    pickle.dump(profile, open(name, 'wb'))

if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog="test",
                                     usage='''

                                         ----------------------------------------------------------------------------------------------------------

                                         This is a habit tracker. For further instructions and help use -h
                                         This habit tracker wil help you to train new habits. It provides ways to create
                                         and delete habits, you can manage your habits and also analyze them.
                                         To use the habit tracker you need to create a profile or load an existing one. 
                                         
                                         The habit tracker then offers the following functions:

                                         1) Create and delete habits -> enter 'create'
                                            Here you can create a new habit, by specifying the name, the quality 
                                            (i.e. if it is a good or a bad habit -> enter good for a good habit) 
                                            and the period (daily or weekly)
                                            of your habit. You can also enter the name of an existing habit, to delete it from your habit list.

                                         2) Analyze habits -> enter ‘analyze‘
                                            Here you can analyze your performance on your habits. You can either analyze a single habit
                                            or get a summary over all habits

                                         3) Manage your habits -> enter ‘manage‘
                                            Here you can check off your habits. If you finished a good habit or if you did not follow a
                                            bad habit, you can save this here.

                                         ----------------------------------------------------------------------------------------------------------

                                         ''',
                                     description='''
                                         This habit tracker wil help you to train new habits. It provides ways to create
                                         and delete habits, you can managa your habits and also analyze them.
                                         ''',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     add_help=True)

    parser.add_argument("argument", type=str, help="Enter something", metavar="HabitTrackerModus")

    arg = parser.parse_args()
    profile_name = arg.argument

    try:
        profile = load_data(profile_name)
    except FileNotFoundError:
        profile = cl.Habit_profile(profile_name)

    while True:
        print("Your current habits:")
        for h in profile.all_habits:
            print(h.name)
        print("You can either analyze, manage or create/delete habits")
        action = input()
        if action == "create" or action == "delete":
            print('''Please enter the follwowing for a good habit: name quality periodicity
            Please enter the following for a bad habit: name quality
            (Quality is either good or bad and periodicity can be either daily or weekly)''')

            profile.create_delete_habit()

        elif action == "manage":


            print('''Which of your good habits did you finish? or Which of your bad habits could'nt you avoid?  :
                               ''')
            fin = input()

            for h in profile.all_habits:
                if h.name == fin:
                    #today = date.today()
                    #past_date = today - timedelta(days=15)
                    #h.dates.append(past_date)
                    h.check_off_habit()

        elif action == "analyze":
            print("To analyze a single habit print: habitname_1")
            print("To get a summary over all habits print: summary_2")
            analysis = input()
            if analysis[-1] == '1':
                for object in profile.all_habits:
                    if object.name == analysis[0:-2]:

                        #today = date.today()
                       # past_date = today - timedelta(days=20)
                        #object.dates.append(past_date)
                        print("")
                        print("--------------------------------------------------------------------------------")
                        object.generate_table()
                        print("\nYour current streak is {time} days long\n".format(time=object.show_me_streak()))
                        print("")
                        print("--------------------------------------------------------------------------------")

            if analysis[-1] == '2':

                profile.summary()

        elif action == "exit":
            break
    save_data(profile, profile_name)