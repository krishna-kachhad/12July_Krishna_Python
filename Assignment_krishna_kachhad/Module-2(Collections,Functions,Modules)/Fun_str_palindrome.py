# Write a Python function that checks whether a passed string is palindrome or not.
'''A string is said to be a palindrome if the reverse of the string is the same as the string. 
   For example, “radar”, "madam", "malayalam" is a palindrome'''


#----------------------Using the reverse and compare method --------------------------

#Define a function 
def palindrome(string):
    if(string == string[::-1]):
        return "The string is a palindrome."
    else:
        return "The string is not a palindrome."
    
#Enter input string
string = input("Enter String: ")
print(palindrome(string))

#-----------------------Using inbuilt reversed function--------------------------------

def isPalindrome(s):
 
    # Using predefined function to # reverse to string print(s)
    rev = ''.join(reversed(s))
 
    # Checking if both string are # equal or not
    if (s == rev):
        return True
    return False
 
# main function
s = input("Enter String: ")
ans = isPalindrome(s)
 
if (ans):
    print("Yes, string is palindrome")
else:
    print("No")