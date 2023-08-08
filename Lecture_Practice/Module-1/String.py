mystr='hello! welcome to my home.'

print(mystr)
print(mystr[0]) #start with 0 index, return first character
print(mystr[-1] )#return last character

#string slice
print(mystr[0:4]) # return range of character, 0 to 3
print(mystr[6:]) #output: e to my home
print(mystr[:9]) #output: welcome t

print(len(mystr)) #return the length of string including spacial char
#length counting with 1 ------ 

#------------=======String Method========---------------

print(mystr)
print(mystr.strip()) #remove the strating and ending space of string
print(mystr.lower()) #returns the string in lower case: all char
print(mystr.upper()) #returns the string in upper case:
print(mystr.replace('l','A'))
print(mystr.replace('Hello!','Hi!')) #replace whole word

print(mystr.capitalize()) #capital first letter of string
print(mystr.casefold()) #same as lower method
print(mystr.count('o')) #how many times 'o' available in string

#-------------startswith and endswith used for validation (form)----------------
print(mystr.startswith('Hello')) #returns true or false, if word or character match with original string returns true
print(mystr.endswith('.')) #returns true or false

#index and find method works same
print(mystr.index('w')) #returns index no of character
print(mystr.find('m')) #returns index no of character

#------starting with 'is' method returns only boolean value(true,false), nd no need to give argument()----
print(mystr.isalpha()) #string is alphabet without space, returns true
print(mystr.isdigit()) #string is digit ,return true 
print(mystr.isalnum()) #{isalphanumeric} string is alphabet or number or both,returns true
print(mystr.islower()) #if all characters are lower case,returns true
print(mystr.isupper()) #if all characters are upper case, returns true
print(mystr.title()) #first letter of string become capital