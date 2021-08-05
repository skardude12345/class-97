'''my first python program'''

myName = 'my name is souhardya'
print(myName)

age = int (input('enter your age: '))

if(age > 18):
    print("you're an adult")
elif age>12:
    print ("you're a teenager")    
else:
    print("you're a kid")

myFriendList = ['Leo', 'Pietro', 'Kabir']

for f in myFriendList:
    print(f)

count = 5
while count >= 0:
    print(count)
    count-= 1
