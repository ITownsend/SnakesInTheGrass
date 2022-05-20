import turtle
#Exercise1
'''toys = ['cars', 'cards', 'guns', 'bears']
foods = ['chicken', 'pizza','ramen', 'sushi']
favourites = toys + foods
print(favourites)'''

#Exercise2
'''
print('There are 8 chocolates in each box and 3 chocolates in each bag')
boxes = int(input('Enter the amount of boxes of chocolate : '))
bags = int(input('Enter the amount of bags of chocolates: '))
tBoxes = 8 * boxes
tBags = 3 * bags
tChocolates = tBoxes + tBags
print('Chocolates in Boxes: ', + tBoxes)
print('Chocolates in Bags: ', + tBags)
print('Total Number of Chocolates: ', + tChocolates)
'''

#Exercise3
'''
myText = 'Hello %s, how are you today?'
fName = input('Enter Name: ')
print(myText % fName)
'''

#Exercise 4
'''for i in range(0, 20):
    print('hello %s' % i)
    if i > 9:
        break
'''


#Exercise5
'''
fMoney = int(input('Enter The amount of money in your bank: ' + '$'))
fInterest = float(input('Enter the amount of interest in decimal Form: ' + ''))
fTime = int(input('Enter how many years it will be in your account: '))
newMoney = 0


for fTime in range(fTime):
    newMoney += (fInterest * fMoney) + fMoney
    print('l %s = %s' % ( fTime, newMoney))
'''














#Practice
'''
age = int(input("Enter Age: "))
if age == 10:
    print('you are 10')
elif age == 11:
    print('you are 11')
elif age == 12:
    print('you are 12')
elif age == 13:
    print('you are 13')
else:
    print('idk')
    '''
'''
age = int(input('enter your age: '))
if age > 1 and age < 100:
    print('you are %s' % age)
else:
    print('huh')
'''
'''
fruit = ['banana', 'apple', 'pear', 'peach']
for i, grape in enumerate(fruit):
    print(i, '. ' + grape, sep='', end=' ')'''
'''
x = int(input('Enter a Number '))
y = int(input('Enter Another Number '))
while x < 50 and y < 100:
    x = x + 1
    y = y + 1
    print(x, y)
'''


