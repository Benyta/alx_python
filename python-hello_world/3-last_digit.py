import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

output = "Last digit of {} is {}"

if last_digit > 5:
    output += " and is greater than 5\n"
elif last_digit == 0:
    output += " and is 0\n"
else:
    output += " and is less than 6 and not 0\n"

print(output.format(number, last_digit))
