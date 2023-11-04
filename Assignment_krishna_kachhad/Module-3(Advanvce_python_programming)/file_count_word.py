# Write a Python program to count the frequency of words in a file.

'''f=open("python_file.txt","w")
f.write("hello, welcome to the python text file")
f.close()'''


import re
frequency = {}
file = open('python.txt', 'r')
text_string = file.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)

# At this point, we want to find the frequency of each word in the document. The suitable concept to use here 
# is Python's Dictionaries, since we need key-value pairs, where key is the word, and the value represents 
# the frequency with which words appeared in the document.
# Assuming we have declared an empty dictionary frequency = { }, the above paragraph would look as follows:
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
    
frequency_list = frequency.keys()
for words in frequency_list:
    print(words, frequency[words])