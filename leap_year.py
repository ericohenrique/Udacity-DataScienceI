##############################################################################################
## This script calculate the number of days from a given date, like the birthdate to today  ##
##  writen by Rodrigo P Maruyama in 14/08/2017                                              ##
##	Udacity - Data Science fundamentals I Nanodegree                                        ##
##############################################################################################

import datetime
import argparse

# This function returns True if the year is a Leap year or False if it is not a Leap year
def is_a_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False
    return

# Get the argument from the command line
parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
birthday = args.echo
# Take the birthdate and split then into 3 variables and set to integer
birthday = birthday.split('/')
b_day = int(birthday[0])
b_month = int(birthday[1])
b_year = int(birthday[2])

# Initialize variable 'days'
days = 0

# declare two lists, one for the days for each month in a leap year and other for regular year
leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
regular_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Get the today date and split then into day, month and year in a integer variable
t = datetime.datetime.now()
t_day = int(t.day)
t_month = int(t.month)
t_year = int(t.year)

#### Check if the Birthday year is greater than the current year
if t_year > b_year:
    for i in range(b_year, t_year+1):
        print("ano -->>> %s" % i)
##### Caso em que o ano atual eh igual ao de nascimento
        if i == b_year: #IF 1
            if b_month == 12:
                days = days + regular_year[12] - b_day
                print("IF 1 %s -->> %s" % i, days)
            else:
                #print("mes de nascimento NAO eh dezembro")
                for j in range(b_month-1, 12):
                    if j == b_month-1:
                        if is_a_leap_year(i):
                            print("IF 2 L month:{0} -->>> {1}+{2}" .format(j+1, days, leap_year[j]-b_day))
                            days = days + leap_year[j] - b_day
                        else:
                            print("IF 2 R month:{0} -->>> {1}+{2}" .format(j+1, days, leap_year[j]-b_day))
                            days = days + regular_year[j] - b_day
                    # count the days in the rest of the year
                    else:
                        if is_a_leap_year(i):
                            print("IF 3 L month:{0} -->> {1}+{2}" .format(j+1, days, leap_year[j]))
                            days = days + leap_year[j]
                        else:
                            print("IF 3 R month:{0} -->> {1}+{2}" .format(j+1, days, regular_year[j]))
                            days = days + regular_year[j]
##### Caso em que os anos estao entre o ano de nascimento e o ano atual
        elif i > b_year and i < t_year:
            for j in range(0, 12):
                if is_a_leap_year(i):
                    print("IF 4 L month:{0} -->> {1}+{2}" .format(j+1, days, leap_year[j]))
                    days = days + leap_year[j]
                else:
                    print("IF 4 R month:{0} -->> {1}+{2}" .format(j+1, days, regular_year[j]))
                    days = days + regular_year[j]
###### Caso em que o ano eh igual ao ano atual
        else: #if i == t_year:
            if t_month == 1:
                days = days + t_day
                print("IF 5 -->>> %s" % days)
            else:
                for j in range(0, t_month):
                    # count the days in the month of birth
                    if j == t_month-1:
                        print("IF 6   month:{0} -->> {1}+{2}" .format(j+1, days, t_day))
                        days = days + t_day
                    else:
                        if is_a_leap_year(i):
                            print("IF 7 R month:{0} -->> {1}+{2}" .format(j+1, days, regular_year[j]))
                            days = days + leap_year[j]
                        else:
                            print("IF 7 R month:{0} -->> {1}+{2}" .format(j+1, days, regular_year[j]))
                            days = days + regular_year[j]
        #else:
            #break
else:
    print("->Caso em que o ano de nascimento eh igual ao ano atual")
    if b_month == t_month:
        print("-->mes de nascimento eh igual ao mes atual")
        days = t_day - b_day
        print("IF 8   month:{0} -->>> {1}-{2}" .format(t_month,t_day,b_day))
    else:
        for j in range(b_month-1, t_month):
            # count the days in the month of birth
            if j == b_month-1:
                if is_a_leap_year(b_year):
                    print("IF 9 L month:{0} -->>> {1}-{2}" .format(j+1, leap_year[j], b_day))
                    days = leap_year[j] - b_day
                else:
                    print("IF 9 R month:{0} -->>> {1}-{2}" .format(j+1, regular_year[j], b_day))
                    days = regular_year[j] - b_day
            # count the days in the rest of the year
            elif j < t_month:
                if is_a_leap_year(b_year):
                    print("IF 10 L month:{0} -->>> {1}+{2}" .format(j+1, days, leap_year[j]))
                    days = days + leap_year[j]
                else:
                    print("IF 10 R month:{0} -->>> {1}+{2}" .format(j+1, days, regular_year[j]))
                    days = days + regular_year[j]
            elif j == t_month:
                if is_a_leap_year(b_year):
                    print("IF 11 L month:{0} -->>> {1}+{2}" .format(j+1, days, leap_year[j]))
                    days = days + t_day
                else:
                    print("IF 11 R month:{0} -->>> {1}+{2}" .format(j+1, days, regular_year[j]))
                    days = days + t_day
print("\n")
length_days = '#'
for i in range(1,len(str(days))):
	length_days = length_days + '#'
print("###################################{0}" .format(length_days))
print("#### Birthday: {0}/{1}/{2}            ####" .format(b_day,b_month,b_year))
print("#### Today: {0}/{1}/{2}               ####" .format(t_day,t_month,t_year))
print("#### The number of the days: {0}  ####" .format(days))
print("###################################{0}" .format(length_days))
