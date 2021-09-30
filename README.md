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

# Testing the Habit Tracker

To test the habit tracker the file test_habit can be used. For this purpose, different data sets are available, each with different habits and test data.

Test data set 1:

Habits:  
Daily habit: workout  
Weekly habit: gaming  
Monthly habit: hiking  
Bad habit: 

Sample data for habit workout:  

+------------+  
|   Dates    |  
+------------+  
| 2021-01-01 |  
| 2021-01-02 |  
| 2021-01-03 |  
| 2021-01-04 |  
| 2021-02-01 |  
| 2021-01-03 |  
| 2021-02-05 |  
| 2021-07-01 |  
| 2021-08-25 |  
| 2021-08-26 |  
| 2021-08-27 |  
| 2021-08-28 |  
+------------+  

Number of no breaks last month: 4
Maximum streak length: 4 days (2021-01-01, 2021-01-02, 2021-01-03, 2021-01-04 or 2021-08-25, 2021-08-26, 2021-08-27, 2021-08-28)  
Current streak length: 0 days


Sample date for habit gaming:

+------------+  
|   Dates    |  
+------------+  
| 2021-01-01 |  
| 2021-01-08 |  
| 2021-01-16 |  
| 2021-02-04 |  
| 2021-02-09 |  
| 2021-02-23 |  
| 2021-08-29 |  
+------------+  
 
Number of no breaks last month: 1  
Maximum streak length: 3 weeks (2021-01-01, 2021-01-08, 2021-01-16)    
Current streak length: 0 weeks  


Sample data for habit kiking:

+------------+  
|   Dates    |  
+------------+  
| 2020-12-01 |  
| 2021-01-08 |  
| 2021-02-16 |  
| 2021-03-04 |  
| 2021-05-09 |  
| 2021-07-23 |  
| 2021-08-31 |  
+------------+  

Number of no breaks last month: 1  
Maximum streak length: 4 months (2020-12-01, 2021-01-08, 2021-02-16, 2021-03-04)    
Current streak length: 2 months (2021-07-23, 2021-08-31)  

Sample data for habit smoking:

+------------+  
|   Dates    |  
+------------+  
| 2020-08-01 |  
| 2020-09-03 |  
| 2020-09-04 |  
| 2020-09-05 |  
| 2020-09-06 |  
| 2021-09-07 |  
| 2021-09-08 |  
| 2021-09-09 |  
| 2021-09-10 |  
| 2021-09-28 |  
+------------+  

Number of breaks last month: 0  
Maximum streak length: 366 days (from 2020-09-06 to 2021-09-07)    
Current streak length: 0 days  

Sample data for habit homework:

+------------+  
|   Dates    |  
+------------+  
| 2021-08-25 |  
| 2021-08-26 |  
| 2021-08-27 |  
| 2021-08-28 |  
| 2020-09-03 |  
| 2020-09-04 |  
| 2020-09-05 |  
| 2020-09-06 |  
| 2021-09-07 |  
| 2021-09-08 |  
| 2021-09-09 |  
| 2021-09-10 |  
| 2021-09-11 |  
| 2021-09-28 |  
+------------+  
  
Number of no breaks last month: 3  
Maximum streak length: 5 days (2021-09-07, 2021-09-08, 2021-09-09, 2021-09-10, 2021-09-11)    
Current streak length: 1 day (2021-09-28)

# Creating new test data

To test the habit tracker with new data just create a csv file as the one provided in the csv folder. Then run test_csv.py, where you create a new habit (just like in the main program) which is then saved with the new data as "Test_profile.pkl". This file can then be used with unit_test.py, where you just replace the name of the profile you want to test. All values that are to be calculated from the new data must be replaced before running the program.  
