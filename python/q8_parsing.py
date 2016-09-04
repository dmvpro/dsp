# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv
import pandas as pd
import urllib2

url = 'https://raw.githubusercontent.com/dmvpro/dsp/master/python/football.csv'

def min_goal_dif(fname, col1, col2, result_col): #define function and columns
    data = pd.read_csv(urllib2.urlopen(fname))   #import csv from url
    abs_goal_var = abs(data[col1] - data[col2])  #calc abs variance between scored/allowed
    min_var = data[abs_goal_var == abs_goal_var.min()]  #find the absolute min
    return min_var[result_col].values[0]         #output team name from column 1

team = min_goal_dif(url, 'Goals', 'Goals Allowed', 'Team')
print team
