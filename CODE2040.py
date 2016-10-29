
import requests
import json

#
# STEP 1: Introduction-------------------------------------------------------------------------------------
#
print('### Step 1 Introduction: Begin <-------------------------------------------------------------------------------------')
token = '3f207b5e8d2a553ef0533a08d76efbe1'

github = 'https://github.com/robertXavierMaldonado/CODE2040-API-Test'

payloadd = {'token': token, 'github': github}
introduction = requests.post('http://challenge.code2040.org/api/register', params=payloadd)
print('###', introduction.text, '<-------------------------------------------------------------------------------------')
print()

#
# STEP 2: Reverse a String-------------------------------------------------------------------------------------
#
print('### Step 2 Reverse a String: Begin <-------------------------------------------------------------------------------------')

token = '3f207b5e8d2a553ef0533a08d76efbe1'
payload = {'token': token}

string_reverse_challenge = requests.post('http://challenge.code2040.org/api/reverse', params=payload)
# Post always sends something

string = string_reverse_challenge.text[::-1] #This is the reversed string

payload1 = {'token': token, 'string': string}
string_reverse_validate = requests.post('http://challenge.code2040.org/api/reverse/validate', params=payload1)
print('###', string_reverse_validate.text, '<-------------------------------------------------------------------------------------')
print()

#
# STEP 3: Needle in a Hatstack---------------------------------------------------------------------------------
#
print('### Step 3 Needle in a Haystack: Begin <-------------------------------------------------------------------------------------')

needle_haystack_challenge = requests.post('http://challenge.code2040.org/api/haystack', params=payload)
response_part3 = json.loads(needle_haystack_challenge.text)
str_needle = response_part3['needle'] #str_needle is the string we are going to search for in haystack
lst_haystack = response_part3['haystack'] #lst_haystack is the list we are going to find str_needle in

print("This is the string I will be looking for:", str_needle)
print("This is the list I will searching through:", lst_haystack)
print()

needle = []

for i in range(len(lst_haystack)):
    if lst_haystack[i] == str_needle:
        print('We have a match!')
        needle = i
    else:
        print('Not yet......')
print()
print('This is the index value for needle, return it:', needle)
print()

payload2 = {'token': token, 'needle': needle}
needle_haystack_validate = requests.post('http://challenge.code2040.org/api/haystack/validate', params=payload2)
print('###', needle_haystack_validate.text, '<-------------------------------------------------------------------------------------')
print()

#
# Step 4: Prefix-----------------------------------------------------------------------------------------------
#
print('### Step 4 Prefix: Begin <-------------------------------------------------------------------------------------')


prefix_array_challenge = requests.post('http://challenge.code2040.org/api/prefix', params=payload)
response_step4 = json.loads(prefix_array_challenge.text)

prefix_for_challenge = response_step4['prefix'] #The prefix we are going to use to sort out the array
array_for_prefixes = response_step4['array'] #The array we are going to look through

print()
print("This is the prefix:", prefix_for_challenge)
print()
print("This is the array I will search through:", array_for_prefixes)
print()

# Compare the prefix with an index
array_diff = []
array_same = []

for i in range(len(array_for_prefixes)):
    if (prefix_for_challenge in array_for_prefixes[i]) == True:
        array_same.append(array_for_prefixes[i])
    else:
        array_diff.append(array_for_prefixes[i])

print("POST this array:", array_diff)

payload3 = {'token': token, 'array': array_diff}

prefix_array_validate = requests.post('http://challenge.code2040.org/api/prefix/validate', json=payload3)

#
# !!!!!Using the json=payload3 tells the API that I am sending JSON!!!!!
#

print("###" + prefix_array_validate.text, '-------------------------------------------------------------------------------------')
print()

#
#Step 5: The Dating Game----------------------------------------------------------------------------------
#

print('### Step 5 The Dating Game: Begin <-------------------------------------------------------------------------------------')
from collections import namedtuple

dating_challenge = requests.post('http://challenge.code2040.org/api/dating', params=payload)
response_step5 = json.loads(dating_challenge.text)

date_stamp = response_step5['datestamp']
interval = response_step5['interval']

print('Date Stamp String: ', date_stamp)
print('Interval str in seconds: ', interval)

"""
I knew that there had to be an easier way to solve this challenge, but it was the close to the deadline and I decided
to go with a weird idea I had.
"""

"""
Here I used indexing to pull information from the date_stamp
Then I turned all the info into integers so that I could use them like numbers.
"""

print()

print("Info from 'date_stamp': ")
date_year = int(date_stamp[0:4])
print('date_year = ', date_year)

date_month = int(date_stamp[5:7])
print('date_month = ', date_month)

date_day = int(date_stamp[8:10])
print('date_day = ', date_day)

date_hrs = int(date_stamp[11:13])
print('date_hrs = ', date_hrs)

date_mins = int(date_stamp[14:16])
print('date_mins = ', date_mins)

date_seconds = int(date_stamp[17:19])
print('date_seconds = ', date_seconds)

print()

"""
Then I divided the 'interval' of seconds into different sections: secs, mins, hrs, and days
"""

#!!!!!!!! rem = remainder !!!!!!!!#

inter_min = interval // 60
inter_sec = interval % 60
inter_hr = inter_min // 60
inter_min_rem = inter_min % 60
inter_days = inter_hr // 24
inter_hr_rem = inter_hr % 24

print("Info from 'interval':")
print('inter_sec =  ', inter_sec)
print('inter_min_rem = ', inter_min_rem)
print('inter_hr_rem = ', inter_hr_rem)
print('inter_days = ', inter_days)
"""
I realized that I needed to return a datetime that had the correct number of days for whatever month was presented to me.
So I created a list of namedtuple objects. I stored the # of day info in each month object
"""

# Make Month Objects to use in the final addition process
Months = namedtuple('Months', 'month number_of_days')
January = Months('January', 31)
February = Months('February', 29)
March = Months('March', 31)
April = Months('April', 30)
May = Months('May', 31)
June = Months('June', 30)
July = Months('July', 31)
August = Months('August', 31)
September = Months('September', 30)
October = Months('October', 31)
November = Months('November', 30)
December = Months('December', 31)
# Make a list of the Months for easier access
list_of_months = [January, February, March, April, May, June, July, August, September, October, November, December]



"""
This is the pseudocode that I created to get an idea of what I needed to do
    1) Add the seconds. Check if the sum is >60, if it is then divide by 60. Leave the remainder and move the minute(s) up
    2) Add the minutes, including the minutes from the last process. If the sum is > 60 then divide by 60. Leave the remainder and move the hr(s) up.
    3) Add the hours, including the hours from the last process. If the sum is > 24 then divide by 24. Leave the remainder and move the day(s) up.
    4) Add the days, including the day(s) from the last process. Use an if statement to check if the sum of days is greater than the current months days,
        if it is then increase the month by 1 and add the remainder to the days.
        - Also check if the number of months is greater than 12, if it is increase the year

I then created a few variable that I would use in this process
"""

final_sec = 0
final_sec_rem = 0

final_min = 0
final_min_rem = 0

final_hr = 0
final_hr_rem = 0

final_day = 0
final_day_rem = 0

final_month = 0
final_month_rem = 0

final_year = 0

# ------------------------------> Start Adding <------------------------------ #

# At the end of this process, only the final_( )_rem variables are used

final_sec = date_seconds + inter_sec
# Add the sec from the interval and date_stamp
final_sec_rem = final_sec % 60
# Find the rem of secs
print()
print('final_sec_rem: ', final_sec_rem)
#print('final_sec:     ', final_sec)
print()

final_min = (final_sec//60) + date_mins + inter_min_rem
# Add the minute(s) from final_sec, interval, and date_stamp
final_min_rem = final_min % 60
# Find the rem of mins
print('final_min_rem: ', final_min_rem)
#print('final_min:     ', final_min)
print()

final_hr = (final_min//60) + date_hrs + inter_hr_rem
# Add the hour(s) from final_sec, interval, and date_stamp
final_hr_rem = final_hr % 24
# Find the rem
print('final_hr_rem:  ', final_hr_rem)
#print('final_hr:      ', final_hr)
print()

final_day = (final_hr//24) + date_day + inter_days
# Add the day(s) from final_hr, interval, and date_stamp

month_index = (date_month - 1)

if final_day <= list_of_months[month_index].number_of_days:
    # If final_day is lower than that month's max num of days, then leave it alone
    # Since month and year are not being changed, assign the date_stamp values to the final_
    final_day_rem = final_day
    final_month_rem = date_month
    final_year = date_year
else:
    # Since their is more days, find the number of days in the new month and increase the month by 1
    # Also! Check if the month number goes over 12, if it does, increase the year by 1
    final_day_rem = final_day  % list_of_months[month_index].number_of_days
    final_month = date_month + 1
    if final_month <= 12:
        final_month_rem = final_month
        final_year = date_year
    else:
        final_month_rem = final_month % 12
        final_year = date_year + 1
    # If final_day is higher than the month's max num of days, then increase the
    # Month by 1, make the rem. Also increase the year if months go over 12

#print('final_day:     ', final_day)
print('final_day_rem: ', final_day_rem)
print()

#print('final_month:    ', final_month)
print('final_month_rem:', final_month_rem)
print()

print('final_year:     ', final_year)
print()

"""
I used each each of the final_()_values to create a string in the ISO 8601 format,
However, I found that the API was sending back an error message because if any of
the number values was > 10, it would be accompanied with a zero. So I had to create
process that would find the numbers > 10 and add a zero to the string value, while
also putting the values into str() format
"""

# Printed out each str() to check if the zero was being added #

final_sec_rem_str = ''
if final_sec_rem < 10:
    final_sec_rem_str = '0' + str(final_sec_rem)
else:
    final_sec_rem_str = str(final_sec_rem)
print(final_sec_rem_str)

final_min_rem_str = ''
if final_min_rem < 10:
    final_min_rem_str = '0' + str(final_min_rem)
else:
    final_min_rem_str = str(final_min_rem)
print(final_min_rem_str)


final_hr_rem_str = ''
if final_hr_rem < 10:
    final_hr_rem_str = '0' + str(final_hr_rem)
else:
    final_hr_rem_str = str(final_hr_rem)
print(final_hr_rem_str)


final_day_rem_str = ''
if final_day_rem < 10:
    final_day_rem_str = '0' + str(final_day_rem)
else:
    final_day_rem_str = str(final_day_rem)
print(final_day_rem_str)

final_month_rem_str = ''
if final_month_rem < 10:
    final_month_rem_str = '0' + str(final_month_rem)
else:
    final_month_rem_str = str(final_month_rem)
print(final_month_rem_str)

final_year_str = str(final_year)
print(final_year_str)

# Use each of the final string values to create a string in the ISO 8601 format
datestamp_string = (final_year_str + '-' + final_month_rem_str + '-' + final_day_rem_str + 'T' + final_hr_rem_str + ':' + final_min_rem_str + ':' + final_sec_rem_str + 'Z')
print("POST this string:", datestamp_string)

payload4 = {'token': token, 'datestamp': datestamp_string}
dating_challenge_validate = requests.post('http://challenge.code2040.org/api/dating/validate',json=payload4)

print("### " + dating_challenge_validate.text, '<-------------------------------------------------------------------------------------')
print()

# :)