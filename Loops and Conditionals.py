#4.1
secret: int = 5
guess: int = 7 

if guess == secret:
    print('just right')
elif guess < secret:
    print('too low')
else:
    print('too high')

#4.2
small: bool = True
green: bool = False

if small and green:
    print('you have a pea')
elif small and not green:
    print('you have a cherry')
elif not small and green:
    print('you have a watermelon')
else:
    print('you have a pumpkin')

#6.1
numbers: list = [3, 2, 1, 0]   
for number in numbers:
    print(number)

#6.2
guess_me: int = 7 
number: int = 1 
while True:
    if number < guess_me:
        print('too low')
    elif number > guess_me:
        print('oops')   
        break 
    elif number == guess_me:
        print('found it!')
        break
    number += 1

#6.3
guess_me: int = 5
for number in range(10):
    if number < guess_me:
        print('too low')
    
    elif number == guess_me:
        print('found it!')
        break        
    else:
        print('oops')   
        break 