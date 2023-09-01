# import regular expression module 
import re

#  create a function to validate the data inputed 
def is_validated_data(data):

# verify data is a string
    if type(data) != str:
        raise ValueError('input value must be string')

# format data  before applying regex, by spliting and joining data.
    formatted_data = ''.join(data.split()) 

# check if data at least a value and contains digit or letter, or combination  using regular expression
    if re.match(r'^(?:[0-9]+|[0-9a-zA-Z]+)$', formatted_data):
        return True



#   Create the palindrome class and initiailze the instance variable.
class Palindrome:

    def __init__(self, input_value):
            
        self.input_value = input_value
#   call is_validated_data to validate data and return error message if required.  
        if not is_validated_data(self.input_value):
            raise ValueError('valid values, should contain only digits and letters')



#   Create is_palindrome function that checks if value is the same as value reversed 
#   [ : : -1] means from begining to end of list in reverse direction
    def is_palindrome(self, value):
        return value == value[ : : -1]
            
#   Create get_palindrome function
    def get_palindrome(self):
#   use list comprehension to get the palindrome by iterating throgh list of inputed values,
#   call is_palindrome function and passing each value as argument to add only palindrome to the list.
        palindrome_list = [value for value in self.input_value.split() if self.is_palindrome(value)]
        return ' '.join(palindrome_list)
        
    
  





# Test Examples
palindrome_object1 = Palindrome('1230321')
print(palindrome_object1.get_palindrome())

palindrome_object2 = Palindrome('1230321 09234 0124210') 
print(palindrome_object2.get_palindrome())

palindrome_object3 = Palindrome('abcd5dcba 1230321 09234 0124210')
print(palindrome_object3.get_palindrome())

palindrome_object4 = Palindrome('kayak 12321 4567654')
print(palindrome_object4.get_palindrome())

palindrome_object5 = Palindrome('programming level 765567 racecar deed')
print(palindrome_object5.get_palindrome())

palindrome_object6 = Palindrome('palindrome hello world')
print(palindrome_object6.get_palindrome())

palindrome_object7 = Palindrome('racecar 765567 45654 coding 98789 radar')
print(palindrome_object7.get_palindrome())

palindrome_object8 = Palindrome('hello abba 7654567 deed kayak world')
print(palindrome_object8.get_palindrome())

palindrome_object9 = Palindrome('programming radar coding')
print(palindrome_object9.get_palindrome())

palindrome_object10 = Palindrome('level 1234321 civic 9876789 radar')
print(palindrome_object10.get_palindrome())








