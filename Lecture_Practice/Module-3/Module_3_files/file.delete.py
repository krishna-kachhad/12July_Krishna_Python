# to make directory through command

import os

#os.remove('newfile.txt') #for file remove

#os.mkdir("Myfolder")

#os.chdir('Myfolder')
#os.mkdir('Subfolder') '''OR'''

os.chdir('Myfolder\Subfolder')
os.mkdir('abc')
os.chdir("abc")
open('abc_sub.txt','x')

#os.chdir('Myfolder\Subfolder')
#os.remove('abc_sub.txt')

'''os.chdir('Myfolder\Subfolder')
os.removedirs('abc')'''