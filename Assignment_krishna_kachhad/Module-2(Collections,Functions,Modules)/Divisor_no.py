# Write a Python program to returns sum of all divisors of a number.
'''For Ex: Sum of Divisor of 8 no = 7-------- 8 = 8*1------8 = 4*2
            sum of divisor = 1 + 2 + 4 = 7
			sum of divisor of 12 no = 1+2+3+4+6 = 16'''


num = int(input("Enter the Number :"))
div = [1]
for i in range(2, num):
	if (num % i)==0:
		div.append(i)
print("Sum of All Divisors :",sum(div))


#----------------------Using function--------------------------
def sum_div(number):
    divisors = [1]
    for i in range(2, number):
        if (number % i)==0:
            divisors.append(i)
    return sum(divisors)
print(sum_div(8))
print(sum_div(12))