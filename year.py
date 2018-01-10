print('This program evaluates the year of the user input')

year = eval(input('Enter the year between 1982-2048'))

a = year%19
b = year%4
c = year%7
d = (19*a+24)%30
e = (2*b + 4*c + 6*d + 5)%7
print(22 + d + e)

date = []

for i in range(31):
    date.append(i+1)

if 22 + d + e in date:
    print('You have entered a correct year i:e {}'.format(year))

else:
    print('\nYou have entered a wrong year')
