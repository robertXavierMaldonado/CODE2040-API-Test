# # requests only works for python 2 in my local machine
# import requests, json

# # making the request by using the library
# # might need to install requests library 

# r = requests.get("http://api.icndb.com/jokes/random")

# # grabbing the json response
# json_response = r.text

# print ("***this is your json response***\n")
# print(json_response)
# print('\n')

# # converting the json response into a json object, json object makes it 
# # easier to parse the json string
# j = json.loads(r.text)

# # grabbing the values 

# print("***grabbing the joke***")
# joke = j["value"]["joke"]
# print(joke)
# print('\n')

# print("***grabbing the id***")
# id = j["value"]["id"]
# print(id)
# print('\n')

# print("***grabbing the type***")
# type = j["type"]
# print(type)

# requests only works for python 2 in my local machine

import requests
import json

#
#STEP 1: Introduction-------------------------------------------------------------------------------------
#
#

token = '3f207b5e8d2a553ef0533a08d76efbe1'

github = 'https://github.com/robertXavierMaldonado/CODE2040-API-Test'

payloadd = {'token': token, 'github': github}
introduction = requests.post('http://challenge.code2040.org/api/register', params=payloadd)
print('*********', introduction.text)
print()

#
#
#STEP 2: Reverse a String-------------------------------------------------------------------------------------
#
#

token = '3f207b5e8d2a553ef0533a08d76efbe1'
payload = {'token': token}

string_reverse_challenge = requests.post('http://challenge.code2040.org/api/reverse', params=payload)
#post always sends something

string = string_reverse_challenge.text[::-1] #This is the reversed string

payload1 = {'token': token, 'string': string}
string_reverse_validate = requests.post('http://challenge.code2040.org/api/reverse/validate', params=payload1)
print('************', string_reverse_validate.text)
print()

#
#
#STEP 3: Needle in a Hatstack---------------------------------------------------------------------------------
#
#

needle_haystack_challenge = requests.post('http://challenge.code2040.org/api/haystack', params=payload)
response_part3 = json.loads(needle_haystack_challenge.text)
str_needle = response_part3['needle'] #str_needle is the string we are going to search for in haystack
lst_haystack = response_part3['haystack'] #lst_haystack is the list we are going to find str_needle in

print(str_needle)
print(lst_haystack)
print()

needle = []

for i in range(len(lst_haystack)):
    if lst_haystack[i] == str_needle:
        print('We have a match!')
        needle = i
    else:
        print('Not yet......')
print(needle)

payload2 = {'token': token, 'needle': needle}
needle_haystack_validate = requests.post('http://challenge.code2040.org/api/haystack/validate', params=payload2)
print('*********', needle_haystack_validate.text)
print()

#
#
#Step 4: Prefix-----------------------------------------------------------------------------------------------
#
#

prefix_array_challenge = requests.post('http://challenge.code2040.org/api/prefix', params=payload)
print(prefix_array_challenge.text)
response_step4 = json.loads(prefix_array_challenge.text)

prefix_for_challenge = response_step4['prefix'] #The prefix we are going to use to sort out the array
array_for_prefixes = response_step4['array'] #The array we are going to look through

print(prefix_for_challenge)
print()
print(array_for_prefixes)
print()

#Compare the prefix with an index
array_diff = []
array_same = []

for i in range(len(array_for_prefixes)):
    if (prefix_for_challenge in array_for_prefixes[i]) == True:
        array_same.append(array_for_prefixes[i])
    else:
        array_diff.append(array_for_prefixes[i])

print(array_diff)

payload3 = {'token': token, 'array': array_diff}

params = json.dump(payload3).encode('utf8')

prefix_array_validate = requests.post('http://challenge.code2040.org/api/prefix/validate', data=params)
print("*********" + prefix_array_validate.text)
print()

#
#
#Step 5: The Dating Game----------------------------------------------------------------------------------
#
#

dating_challenge = requests.post('http://challenge.code2040.org/api/dating', params=payload)
print(dating_challenge.text)
response_step5 = json.loads(dating_challenge.text)

date_stamp = response_step5['datestamp']
interval = response_step5['interval']

print(date_stamp)
print(interval)
