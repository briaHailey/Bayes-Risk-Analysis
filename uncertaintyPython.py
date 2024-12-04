"""

Name: Bria Weisblat
Date: 2/27/24
Assignment:Assignment # 7
Due Date: 03/03/24
About this project: This project imports the steak risk excel sheet into a
data set and performs/displays various probability calculations.
Assumptions: Since there were 534 participants, some rounding techniques were
used to make the probabilities add to exactly 1.
All work below was performed by Bria Weisblat

"""

import pandas as pd
import os

# Obtain the cwd and file
cwd = os.getcwd()
file = 'steak-risk-survey.xlsx'

# join using os.path
path = os.path.join(cwd,file)

# read file
df = pd.read_excel(path)

#Print all rows and colums
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

""" Variables for each count
Variables will be named var### where the first # is a bool representing 
whether or not the participant smokes, the second # is a bool representing 
whether or not the participant drinks, and the third # is a bool representing
whether or not the participant gambles
"""

# Does not smoke, does not drink, does not gamble
var_000 = 0
#Does not smoke, does not drink, gambles
var_001 = 0
#Does not smoke, drinks, does not gamble
var_010 = 0
# Does not smoke, drinks, gambles
var_011 = 0
#Smokes, does not drink, does not gamble
var_100 = 0
#Smokes, does not drink, gambles
var_101 = 0
#Smokes, drinks, does not gamble
var_110 = 0
#Smokes, drinks, and gambles
var_111 = 0

# Loop through each row in the set
for index, row in df.iterrows():
    # Check for 000
    if row['Do you ever smoke cigarettes?'] == 'No' and \
       row['Do you ever drink alcohol?'] == 'No' and \
       row['Do you ever gamble?'] == 'No':
        var_000 += 1
    # Check for 001
    if row['Do you ever smoke cigarettes?'] == 'No' and \
       row['Do you ever drink alcohol?'] == 'No' and \
       row['Do you ever gamble?'] == 'Yes':
        var_001 += 1
    # Check for 010
    if row['Do you ever smoke cigarettes?'] == 'No' and \
       row['Do you ever drink alcohol?'] == 'Yes' and \
       row['Do you ever gamble?'] == 'No':
        var_010 += 1
    # Check for 011
    if row['Do you ever smoke cigarettes?'] == 'No' and \
       row['Do you ever drink alcohol?'] == 'Yes' and \
       row['Do you ever gamble?'] == 'Yes':
        var_011 += 1
    # Check for 100
    if row['Do you ever smoke cigarettes?'] == 'Yes' and \
       row['Do you ever drink alcohol?'] == 'No' and \
       row['Do you ever gamble?'] == 'No':
        var_100 += 1
    # Check for 101
    if row['Do you ever smoke cigarettes?'] == 'Yes' and \
       row['Do you ever drink alcohol?'] == 'No' and \
       row['Do you ever gamble?'] == 'Yes':
        var_101 += 1
    # Check for 110
    if row['Do you ever smoke cigarettes?'] == 'Yes' and \
       row['Do you ever drink alcohol?'] == 'Yes' and \
       row['Do you ever gamble?'] == 'No':
        var_110 += 1
    # Check for 111
    if row['Do you ever smoke cigarettes?'] == 'Yes' and \
       row['Do you ever drink alcohol?'] == 'Yes' and \
       row['Do you ever gamble?'] == 'Yes':
        var_111 += 1

# This variable keeps track of the number of participants who answered yes or no to each of the three questions
num_participants = var_000 + var_001 + var_010 + var_011 + var_100 + var_101 + var_110 + var_111

#Print the distribution table with count of the data for A1(Smokes?), A2(Drinks?), A3(Gambles?)
print("The following utilizes the steak risk survey data sheet")
print()
print("Distribution table with count of the data for A1(Smokes?), A2(Drinks?), A3(Gambles?)")
print ("-----------------------------------------------------------------------")
print("            |            Smoke           |          Don't Smoke       |")
print ("-----------------------------------------------------------------------")
print("            |Gamble      | Don't Gamble  | Gamble     | Don't Gamble  |")
print ("-----------------------------------------------------------------------")
print ("Drink       | {:<10} | {:<13} | {:<10} | {:<13} |".format(var_111, var_110, var_011, var_010))
print("-----------------------------------------------------------------------")
print ("Don't Drink | {:<10} | {:<13} | {:<10} | {:<13} |".format(var_101, var_100, var_001, var_000))
print("-----------------------------------------------------------------------")

# Create and assign percentage variables for each combo
per_var_000 = round((var_000 / num_participants), 3)
per_var_001 = round((var_001 / num_participants), 3)
per_var_010 = round((var_010 / num_participants), 3)
per_var_011 = round((var_011 / num_participants), 3)
per_var_100 = round((var_100 / num_participants), 3)
per_var_101 = round((var_101 / num_participants), 3)
per_var_110 = round((var_110 / num_participants), 3)
# Here I used the value .106 instead of the calculated .1067 to ensure that the total adds up to 1 exactly
per_var_111 = .106

#Print the distribution table with percentage of the data for A1(Smokes?), A2(Drinks?), A3(Gambles?)
print()
print("Distribution table with the percentage of the data for A1(Smokes?), A2(Drinks?), A3(Gambles?)")
print ("-----------------------------------------------------------------------")
print("            |            Smoke           |          Don't Smoke       |")
print ("-----------------------------------------------------------------------")
print("            |Gamble      | Don't Gamble  | Gamble     | Don't Gamble  |")
print ("-----------------------------------------------------------------------")
print ("Drink       | {:<10} | {:<13} | {:<10} | {:<13} |".format(round(per_var_111,3), round(per_var_110,3), round(per_var_011,3), round(per_var_010,3) ))
print("-----------------------------------------------------------------------")
print ("Don't Drink | {:<10} | {:<13} | {:<10} | {:<13} |".format(round(per_var_101, 3), round(per_var_100,3), round(per_var_001, 3), round(per_var_000, 3) ))
print("-----------------------------------------------------------------------")

#Compute the probability of A1, A2, A3
p_a1_yes = round((per_var_111 + per_var_110 + per_var_101 + per_var_100), 3)
p_a1_no = round((per_var_011 + per_var_010 + per_var_001 + per_var_000), 3)
p_a2_yes = round(per_var_111, 3)  + round(per_var_110, 3) + round(per_var_011, 3) + round(per_var_010, 3)
p_a2_no = round((per_var_101 + per_var_100 + per_var_001 + per_var_000), 3)
p_a3_yes = round((per_var_111 + per_var_011 + per_var_101 + per_var_001), 3)
p_a3_no = round((per_var_110 + per_var_010 + per_var_100 + per_var_000), 3)

#Print the probability of A1, A2, A3
print()
print("P(A1): ")
print("Probability that someone smokes = " + str(p_a1_yes))
print("Probability that someone does not smoke= " + str(p_a1_no))
print()
print("P(A2): ")
print("Probability that someone drinks = " + str(p_a2_yes))
print("Probability that someone does not drink = " + str(p_a2_no))
print()
print("P(A3): ")
print("Probability that someone gambles = " + str(p_a3_yes))
print("Probability that someone does not gamble = " + str(p_a3_no))
print()

# Probability that someone smokes, drinks, or smokes and drinks
var_a1_union_a2 = round(per_var_010, 3) + round(per_var_011, 3) + round(per_var_100, 3) + round(per_var_101, 3) + round(per_var_110, 3) + round(per_var_111, 3)
print("P(A1 v A2): " + str(var_a1_union_a2) )
print()

#Probability that someone smokes and gambles
var_a1_intersection_a3 = round(per_var_101, 3) + round(per_var_111, 3)
print("P(A1, A3): " + str(var_a1_intersection_a3))
print()

#Probability that someone drinks given that we know they smoke and gamble
given_prob1 = per_var_111 / var_a1_intersection_a3
print("P(A2 | A1, A3): " + str(round(given_prob1, 3)))
print()

#Probability that someone smokes and gambles given that we know they drink
bayes_problem = (given_prob1 * var_a1_intersection_a3) / p_a2_yes
print("Using Bayes P(A1, A3| A2): " + str(round(bayes_problem, 3)))



