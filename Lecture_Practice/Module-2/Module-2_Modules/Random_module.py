import random

x=random.random()
x=random.randint(1111,9999)
x=random.randrange(1111,9999,120)
print(x)


captcha=['jj8c','Lcn8','09dS','Lwn7','Rbvs','Pkw8','Nc4s','Lic7','Lm9A']

#x=random.choice(captcha)
#print(x)
print(captcha)
random.shuffle(captcha)
print(captcha)

#---------------------------ppt example-------------------------
import random
number = random.randint(9,20)

while True:
    guess = int(input("Guess number :"))
    
    if guess==number:
        print("Guess number is correct")
        break
    if guess>number:
        print("Guess is greater than number")
    if guess<number:
        print("Guess is small than number")
    else:
        print("You guess the right number")
