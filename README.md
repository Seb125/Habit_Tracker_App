# Habit-tracker

This is a habit tracker. This habit tracker wil help you to train new habits. It provides ways to create and delete habits, you can manage your habits and also analyze them. 

## Requirements

Python >= 3.7

Install all of the required Python libraries.

pip install argparse

pip install pickle-mixin

pip install datetime

pip install prettytable

## Running the Habit Tracker

In the root directory, run the following command (on Mac or Linux) to make the main.py file executable

chmod a+x ./main.py

Run the main.py file to start the Habit Tracker:

python main.py

This will raise an error: the following arguments are required: Profilename.pkl

To use the habit tracker you need to create a profile or load an existing one. Therefore type the following:

python main.py profilename.pkl
 
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
    
    Note: Weekly habits are based on the ISO week date system. 

Help on how to use the Habit Tracker can also be accessed by the follwoing:

python main.py -h
