#Write a Python program to test whether a passed letter is a vowel or not.

ch=input("Enter a character: ")

if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or 
    ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
    print("The character is a vowel!")
else:
    print("The character is a Consonant!")