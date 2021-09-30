import csv
from datetime import date
import pickle
from classes_Kopie import *


def save_data(profile,name):
    '''This function saves a habit_profile in a shelve'''
    pickle.dump(profile, open(name, 'wb'))

liste = []

with open('test_data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        x = row[0].split()
        print(x)
        liste.append(date(int(x[0]), int(x[1]), int(x[2])))

profile_name = "Test_Profile.pkl"
profile = Habit_profile(profile_name)

profile.create_habit()
profile.all_habits[0].dates.extend(liste)

save_data(profile, profile_name)