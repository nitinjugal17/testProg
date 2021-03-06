# -*- coding: utf-8 -*-
from random import randint

# getting 10000 digit number using randint
rand_number = randint(10,9999**5630)

#converting Long int to string for spliting as long doesn't support silicing
rand_number = str(rand_number)
last_index = 0
number_list = []

# creating a list of 4 digit number using silicing of string
for first_index in range(0,10004,4):
    number_list.append(rand_number[last_index:first_index])
    last_index = first_index

# delete first index as it is empty while creating a new empty list
del number_list[:1]
sum_dict = {}

# iterating over list and saving the sum of digits in a form of
# dict_key = to get the number
# dict_value =  to get the sum of number
for num in number_list:
    dict_key = num
    number_split = list(num)
    dict_value = 1
    for digit in number_split:
        digit = int(digit)
        dict_value = dict_value*digit
    sum_dict[dict_key] = dict_value
checksum_list = []

# appending all the sum values to list
for key,value in sum_dict.iteritems():
    checksum_list.append(value)

#getting max value from the list
max_value = max(checksum_list)
print "Max Value" , max_value

#Checking the Key from the highest value
for key,value in sum_dict.iteritems():
     if max_value == value:
         print 'Existing Number From Random List:',key
